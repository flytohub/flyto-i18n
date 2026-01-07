#!/usr/bin/env python3
"""
sync-from-core.py - Sync i18n keys from flyto-core

This script scans flyto-core modules and extracts all i18n keys,
then updates the English base locale files.

Usage:
    python scripts/sync-from-core.py [--core-path PATH] [--dry-run]

Options:
    --core-path    Path to flyto-core (default: ../flyto-core)
    --dry-run      Show changes without writing files
"""

import argparse
import ast
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Any, Optional

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
EN_DIR = LOCALES_DIR / 'en'


def extract_keys_from_file(file_path: Path) -> List[Dict[str, str]]:
    """Extract i18n keys from a Python file."""
    keys = []

    try:
        with open(file_path) as f:
            content = f.read()
    except Exception as e:
        print(f"Warning: Could not read {file_path}: {e}")
        return keys

    # Find @register_module decorators
    # Extract label_key, description_key, and other _key fields

    # Pattern for key assignments
    key_patterns = [
        (r"label_key\s*=\s*['\"]([^'\"]+)['\"]", 'label'),
        (r"description_key\s*=\s*['\"]([^'\"]+)['\"]", 'description'),
        (r"'label_key'\s*:\s*['\"]([^'\"]+)['\"]", 'label'),
        (r"'description_key'\s*:\s*['\"]([^'\"]+)['\"]", 'description'),
    ]

    # Also extract the actual label/description values for English base
    value_patterns = [
        (r"label\s*=\s*['\"]([^'\"]+)['\"]", 'label'),
        (r"description\s*=\s*['\"]([^'\"]+)['\"]", 'description'),
        (r"'label'\s*:\s*['\"]([^'\"]+)['\"]", 'label'),
        (r"'description'\s*:\s*['\"]([^'\"]+)['\"]", 'description'),
    ]

    # Extract key-value pairs
    for key_pattern, field_type in key_patterns:
        for match in re.finditer(key_pattern, content):
            key = match.group(1)

            # Try to find corresponding value
            value = key.split('.')[-1].replace('_', ' ').title()  # Default

            # Look for actual value near this key
            start = max(0, match.start() - 500)
            end = min(len(content), match.end() + 500)
            context = content[start:end]

            for val_pattern, val_type in value_patterns:
                if val_type == field_type:
                    val_match = re.search(val_pattern, context)
                    if val_match:
                        value = val_match.group(1)
                        break

            keys.append({
                'key': key,
                'value': value,
                'type': field_type,
                'source': str(file_path)
            })

    return keys


def scan_core_modules(core_path: Path) -> Dict[str, Dict[str, str]]:
    """Scan all modules in flyto-core and extract keys."""
    modules_dir = core_path / 'src' / 'core' / 'modules'

    if not modules_dir.exists():
        print(f"Error: Modules directory not found: {modules_dir}")
        sys.exit(1)

    all_keys = {}

    for py_file in modules_dir.rglob('*.py'):
        if '__pycache__' in str(py_file):
            continue

        keys = extract_keys_from_file(py_file)
        for item in keys:
            all_keys[item['key']] = item['value']

    return all_keys


def group_by_category(keys: Dict[str, str]) -> Dict[str, Dict[str, str]]:
    """Group keys by category for separate files."""
    grouped = defaultdict(dict)

    for key, value in keys.items():
        parts = key.split('.')
        if len(parts) >= 2:
            if parts[0] == 'modules':
                category = parts[1]  # e.g., 'browser', 'flow'
            elif parts[0] == 'common':
                category = 'common'
            else:
                category = 'other'
        else:
            category = 'other'

        grouped[category][key] = value

    return dict(grouped)


def write_locale_files(grouped_keys: Dict[str, Dict[str, str]], dry_run: bool = False):
    """Write grouped keys to locale files."""
    EN_DIR.mkdir(parents=True, exist_ok=True)

    for category, translations in grouped_keys.items():
        if not translations:
            continue

        filename = f"modules.{category}.json" if category != 'common' else 'common.json'
        file_path = EN_DIR / filename

        data = {
            "$schema": "../../schema/locale.schema.json",
            "locale": "en",
            "category": category,
            "version": "1.0.0",
            "translations": dict(sorted(translations.items()))
        }

        if dry_run:
            print(f"\nWould write {file_path}:")
            print(f"  {len(translations)} keys")
        else:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Wrote {file_path}: {len(translations)} keys")


def main():
    parser = argparse.ArgumentParser(description='Sync keys from flyto-core')
    parser.add_argument('--core-path', default='../flyto-core',
                        help='Path to flyto-core')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show changes without writing')
    args = parser.parse_args()

    core_path = Path(args.core_path).resolve()
    if not core_path.exists():
        print(f"Error: flyto-core not found at {core_path}")
        sys.exit(1)

    print(f"Scanning flyto-core at: {core_path}")

    # Extract keys
    all_keys = scan_core_modules(core_path)
    print(f"Found {len(all_keys)} i18n keys")

    # Group by category
    grouped = group_by_category(all_keys)
    print(f"Categories: {list(grouped.keys())}")

    # Write files
    write_locale_files(grouped, dry_run=args.dry_run)

    print("\nSync complete!")


if __name__ == '__main__':
    main()
