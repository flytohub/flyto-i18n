#!/usr/bin/env python3
"""
validate.py - Validate translation files

Usage:
    python scripts/validate.py [--locale LOCALE] [--strict]

Options:
    --locale    Validate specific locale only
    --strict    Exit with code 1 on any error
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Any

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
SCHEMA_DIR = PROJECT_ROOT / 'schema'


def load_schema() -> Dict:
    """Load locale schema."""
    schema_path = SCHEMA_DIR / 'locale.schema.json'
    with open(schema_path) as f:
        return json.load(f)


def load_base_keys() -> set:
    """Load all keys from English base locale."""
    en_dir = LOCALES_DIR / 'en'
    if not en_dir.exists():
        return set()

    keys = set()
    for json_file in en_dir.glob('*.json'):
        with open(json_file) as f:
            data = json.load(f)
            if 'translations' in data:
                keys.update(data['translations'].keys())
    return keys


def validate_file(file_path: Path, base_keys: set) -> List[Dict]:
    """Validate a single translation file."""
    errors = []

    try:
        with open(file_path) as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append({
            'file': str(file_path),
            'type': 'json_error',
            'message': f'Invalid JSON: {e}'
        })
        return errors

    # Check required fields
    for field in ['locale', 'category', 'version', 'translations']:
        if field not in data:
            errors.append({
                'file': str(file_path),
                'type': 'missing_field',
                'message': f"Missing required field: '{field}'"
            })

    if 'translations' not in data:
        return errors

    translations = data['translations']

    # Validate each translation
    # modules.category.name.field or common.field
    # Allow alphanumeric with underscores in segments (e.g., md5, branch_1, aws_s3)
    key_pattern = re.compile(r'^(modules\.[a-z][a-z0-9_]*\.[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)*|common\.[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)*)$')

    for key, value in translations.items():
        # Check key format
        if not key_pattern.match(key):
            errors.append({
                'file': str(file_path),
                'type': 'invalid_key',
                'key': key,
                'message': f"Invalid key format: '{key}'"
            })

        # Check value type
        if not isinstance(value, str):
            errors.append({
                'file': str(file_path),
                'type': 'invalid_value',
                'key': key,
                'message': f"Value must be string, got {type(value).__name__}"
            })
            continue

        # Check value length
        if len(value) > 500:
            errors.append({
                'file': str(file_path),
                'type': 'value_too_long',
                'key': key,
                'message': f"Value too long ({len(value)} > 500 chars)"
            })

        # Check for potential XSS
        if '<script' in value.lower() or 'javascript:' in value.lower():
            errors.append({
                'file': str(file_path),
                'type': 'security',
                'key': key,
                'message': "Potential script injection detected"
            })

    # Check if keys exist in base (skip for 'en')
    if data.get('locale') != 'en' and base_keys:
        for key in translations.keys():
            if key not in base_keys:
                errors.append({
                    'file': str(file_path),
                    'type': 'unknown_key',
                    'key': key,
                    'message': f"Key not found in base locale: '{key}'"
                })

    return errors


def validate_locale(locale: str, base_keys: set) -> List[Dict]:
    """Validate all files for a locale."""
    locale_dir = LOCALES_DIR / locale
    if not locale_dir.exists():
        return [{'type': 'error', 'message': f"Locale directory not found: {locale}"}]

    all_errors = []
    for json_file in locale_dir.glob('*.json'):
        errors = validate_file(json_file, base_keys)
        all_errors.extend(errors)

    return all_errors


def main():
    parser = argparse.ArgumentParser(description='Validate translation files')
    parser.add_argument('--locale', '-l', help='Validate specific locale')
    parser.add_argument('--strict', action='store_true', help='Exit with code 1 on error')
    args = parser.parse_args()

    base_keys = load_base_keys()

    if args.locale:
        locales = [args.locale]
    else:
        locales = [d.name for d in LOCALES_DIR.iterdir() if d.is_dir()]

    total_errors = 0
    total_files = 0

    for locale in locales:
        locale_dir = LOCALES_DIR / locale
        if not locale_dir.exists():
            continue

        files = list(locale_dir.glob('*.json'))
        total_files += len(files)

        errors = validate_locale(locale, base_keys if locale != 'en' else set())

        if errors:
            print(f"\n[{locale}] {len(errors)} error(s):")
            for error in errors:
                print(f"  - {error.get('file', '')}: {error['message']}")
            total_errors += len(errors)
        else:
            print(f"[{locale}] OK ({len(files)} files)")

    print(f"\n{'=' * 50}")
    print(f"Total: {total_files} files, {total_errors} errors")
    print(f"Status: {'FAIL' if total_errors > 0 else 'PASS'}")

    if args.strict and total_errors > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
