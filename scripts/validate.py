#!/usr/bin/env python3
"""
validate.py - Validate translation files

Usage:
    python scripts/validate.py [--locale LOCALE] [--project PROJECT] [--strict]

Options:
    --locale    Validate specific locale only
    --project   Validate specific project only (cloud, modules, landing, shared)
    --strict    Exit with code 1 on any error
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict, List

from jsonschema import Draft7Validator

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from i18n_contract import PROJECT_DIRS  # noqa: E402

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
SCHEMA_DIR = PROJECT_ROOT / 'schema'

STRICT_PLACEHOLDER_LOCALES = {'zh-TW', 'zh-CN'}
REPLACEMENT_PLACEHOLDER_RE = re.compile(r'\?{3,}')
CRITICAL_NON_EMPTY_PREFIXES = {
    'code': ('code.vaReport.', 'code.communityLoop.'),
}


def load_schema() -> Dict:
    """Load and validate the Draft-07 locale source schema."""
    schema_path = SCHEMA_DIR / 'locale.schema.json'
    with open(schema_path) as f:
        schema = json.load(f)
    Draft7Validator.check_schema(schema)
    return schema


def load_manifest_schema() -> Dict:
    """Load and validate the repository manifest schema."""
    schema_path = SCHEMA_DIR / 'manifest.schema.json'
    with open(schema_path) as f:
        schema = json.load(f)
    Draft7Validator.check_schema(schema)
    return schema


def schema_errors(data: Dict, schema: Dict, file_path: Path) -> List[Dict]:
    """Convert sorted JSON Schema violations into validation findings."""
    findings = []
    validator = Draft7Validator(schema)
    for error in sorted(validator.iter_errors(data), key=lambda item: list(item.absolute_path)):
        location = '.'.join(str(part) for part in error.absolute_path)
        findings.append({
            'file': str(file_path),
            'type': 'schema_error',
            'key': location,
            'message': f"Schema violation{f' at {location}' if location else ''}: {error.message}",
        })
    return findings


def get_locales(project: str = None) -> list:
    """Get available locales by scanning project directories."""
    locales = set()
    dirs = [project] if project else PROJECT_DIRS
    for proj in dirs:
        proj_dir = LOCALES_DIR / proj
        if proj_dir.exists():
            for d in proj_dir.iterdir():
                if d.is_dir():
                    locales.add(d.name)
    return sorted(locales)


def load_base_keys() -> set:
    """Load all keys from English base locale across all projects."""
    keys = set()
    for proj in PROJECT_DIRS:
        en_dir = LOCALES_DIR / proj / 'en'
        if not en_dir.exists():
            continue
        for json_file in en_dir.glob('*.json'):
            with open(json_file, encoding='utf-8') as f:
                data = json.load(f)
                if 'translations' in data:
                    keys.update(data['translations'].keys())
    return keys


def validate_file(file_path: Path, base_keys: set, schema: Dict = None) -> List[Dict]:
    """Validate one locale catalog against schema and business rules."""
    errors = []

    try:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        errors.append({
            'file': str(file_path),
            'type': 'json_error',
            'message': f'Invalid JSON: {e}'
        })
        return errors

    errors.extend(schema_errors(data, schema or load_schema(), file_path))

    if not isinstance(data.get('translations'), dict):
        return errors

    translations = data['translations']
    locale = data.get('locale') or file_path.parent.name
    category = data.get('category') or file_path.stem

    for key, value in translations.items():
        if not isinstance(value, str):
            continue

        if '<script' in value.lower() or 'javascript:' in value.lower():
            errors.append({
                'file': str(file_path),
                'type': 'security',
                'key': key,
                'message': "Potential script injection detected"
            })

        if locale in STRICT_PLACEHOLDER_LOCALES and REPLACEMENT_PLACEHOLDER_RE.search(value):
            errors.append({
                'file': str(file_path),
                'type': 'replacement_placeholder',
                'key': key,
                'message': f"Corrupted replacement placeholder detected in '{key}'"
            })

        critical_prefixes = CRITICAL_NON_EMPTY_PREFIXES.get(category, ())
        if locale in STRICT_PLACEHOLDER_LOCALES and value.strip() == "" and any(
            key.startswith(prefix) for prefix in critical_prefixes
        ):
            errors.append({
                'file': str(file_path),
                'type': 'missing_critical_translation',
                'key': key,
                'message': f"Critical UI translation must not be empty: '{key}'"
            })

    # Check if keys exist in base (skip for 'en' and 'cloud.*' keys)
    if data.get('locale') != 'en' and base_keys:
        for key in translations.keys():
            if key.startswith('cloud.') or key.startswith('landing.'):
                continue
            if key not in base_keys:
                errors.append({
                    'file': str(file_path),
                    'type': 'unknown_key',
                    'key': key,
                    'message': f"Key not found in base locale: '{key}'"
                })

    return errors


def validate_locale(locale: str, base_keys: set, projects: list = None, schema: Dict = None) -> List[Dict]:
    """Validate all files for a locale across project directories."""
    all_errors = []
    dirs = projects or PROJECT_DIRS

    for proj in dirs:
        locale_dir = LOCALES_DIR / proj / locale
        if not locale_dir.exists():
            continue
        for json_file in locale_dir.glob('*.json'):
            errors = validate_file(json_file, base_keys, schema)
            all_errors.extend(errors)

    return all_errors


def count_files(locale: str, projects: list = None) -> int:
    """Count translation files for a locale."""
    count = 0
    dirs = projects or PROJECT_DIRS
    for proj in dirs:
        locale_dir = LOCALES_DIR / proj / locale
        if locale_dir.exists():
            count += len(list(locale_dir.glob('*.json')))
    return count


def main():
    """Validate selected catalogs and return a strict-mode exit status."""
    parser = argparse.ArgumentParser(description='Validate translation files')
    parser.add_argument('--locale', '-l', help='Validate specific locale')
    parser.add_argument('--project', '-p', help='Validate specific project (cloud, modules, landing, shared)')
    parser.add_argument('--strict', action='store_true', help='Exit with code 1 on error')
    args = parser.parse_args()

    projects = [args.project] if args.project else None
    base_keys = load_base_keys()
    locale_schema = load_schema()
    manifest_path = PROJECT_ROOT / 'manifest.json'
    with open(manifest_path, encoding='utf-8') as manifest_file:
        manifest_errors = schema_errors(
            json.load(manifest_file),
            load_manifest_schema(),
            manifest_path,
        )

    if args.locale:
        locales = [args.locale]
    else:
        locales = get_locales(args.project)

    total_errors = len(manifest_errors)
    total_files = 0

    if manifest_errors:
        print(f"[manifest] {len(manifest_errors)} error(s):")
        for error in manifest_errors:
            print(f"  - {error['message']}")
    else:
        print("[manifest] OK")

    for locale in locales:
        files = count_files(locale, projects)
        total_files += files

        errors = validate_locale(
            locale,
            base_keys if locale != 'en' else set(),
            projects,
            locale_schema,
        )

        if errors:
            print(f"\n[{locale}] {len(errors)} error(s):")
            for error in errors:
                print(f"  - {error.get('file', '')}: {error['message']}")
            total_errors += len(errors)
        else:
            print(f"[{locale}] OK ({files} files)")

    print(f"\n{'=' * 50}")
    print(f"Total: {total_files} files, {total_errors} errors")
    print(f"Status: {'FAIL' if total_errors > 0 else 'PASS'}")

    if args.strict and total_errors > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()
