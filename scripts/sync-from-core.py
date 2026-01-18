#!/usr/bin/env python3
"""
sync-from-core.py - Sync i18n keys from flyto-core

This script scans flyto-core modules and extracts all i18n keys,
then updates the English base locale files.

Features:
- Adds new keys from flyto-core
- Updates existing key values
- DELETES keys that no longer exist in flyto-core (cleanup)

Usage:
    python scripts/sync-from-core.py [--core-path PATH] [--dry-run]

Options:
    --core-path    Path to flyto-core (default: ../flyto-core)
    --dry-run      Show changes without writing files
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set

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

            # Skip dynamic keys (f-strings, template literals, function calls)
            if '{' in key or '(' in key or '$' in key or '`' in key:
                continue

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


def scan_core_modules(core_path: Path) -> Dict[str, str]:
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
            elif parts[0] == 'schema':
                category = 'other'  # schema.field.* goes to other
            else:
                category = 'other'
        else:
            category = 'other'

        grouped[category][key] = value

    return dict(grouped)


def load_existing_keys() -> Dict[str, Set[str]]:
    """Load existing keys from all locale files."""
    existing = defaultdict(set)

    if not EN_DIR.exists():
        return dict(existing)

    for json_file in EN_DIR.glob('*.json'):
        try:
            with open(json_file) as f:
                data = json.load(f)

            category = data.get('category', 'other')
            translations = data.get('translations', {})
            existing[category] = set(translations.keys())
        except Exception as e:
            print(f"Warning: Could not read {json_file}: {e}")

    return dict(existing)


def write_locale_files(
    grouped_keys: Dict[str, Dict[str, str]],
    existing_keys: Dict[str, Set[str]],
    dry_run: bool = False
) -> Dict[str, Dict]:
    """Write grouped keys to locale files. Returns stats."""
    EN_DIR.mkdir(parents=True, exist_ok=True)

    stats = {
        'added': 0,
        'updated': 0,
        'deleted': 0,
        'categories': {}
    }

    # Get all categories (both new and existing)
    all_categories = set(grouped_keys.keys()) | set(existing_keys.keys())

    for category in all_categories:
        new_translations = grouped_keys.get(category, {})
        old_keys = existing_keys.get(category, set())
        new_keys = set(new_translations.keys())

        # Calculate changes
        added = new_keys - old_keys
        deleted = old_keys - new_keys
        kept = new_keys & old_keys

        cat_stats = {
            'added': len(added),
            'deleted': len(deleted),
            'total': len(new_translations)
        }
        stats['categories'][category] = cat_stats
        stats['added'] += len(added)
        stats['deleted'] += len(deleted)

        filename = f"modules.{category}.json" if category != 'common' else 'common.json'
        file_path = EN_DIR / filename

        if not new_translations:
            # Category has no keys anymore - delete file
            if file_path.exists():
                if dry_run:
                    print(f"Would DELETE {file_path} (all keys removed)")
                else:
                    file_path.unlink()
                    print(f"DELETED {file_path} (all keys removed)")
            continue

        data = {
            "$schema": "../../schema/locale.schema.json",
            "locale": "en",
            "category": category,
            "version": "1.0.0",
            "translations": dict(sorted(new_translations.items()))
        }

        change_info = []
        if added:
            change_info.append(f"+{len(added)} added")
        if deleted:
            change_info.append(f"-{len(deleted)} deleted")
        change_str = f" ({', '.join(change_info)})" if change_info else ""

        if dry_run:
            print(f"Would write {file_path}: {len(new_translations)} keys{change_str}")
            if deleted:
                for key in sorted(deleted)[:5]:
                    print(f"  - DELETE: {key}")
                if len(deleted) > 5:
                    print(f"  ... and {len(deleted) - 5} more")
        else:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"Wrote {file_path}: {len(new_translations)} keys{change_str}")

    return stats


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

    # Load existing keys first
    existing_keys = load_existing_keys()
    existing_count = sum(len(keys) for keys in existing_keys.values())
    print(f"Existing keys in flyto-i18n: {existing_count}")

    # Extract keys from core
    all_keys = scan_core_modules(core_path)
    print(f"Found {len(all_keys)} i18n keys in flyto-core")

    # Group by category
    grouped = group_by_category(all_keys)
    print(f"Categories: {list(grouped.keys())}")

    # Write files (with delete support)
    stats = write_locale_files(grouped, existing_keys, dry_run=args.dry_run)

    print()
    print("=" * 50)
    print(f"Summary: +{stats['added']} added, -{stats['deleted']} deleted")
    print("=" * 50)
    print("\nSync complete!")


if __name__ == '__main__':
    main()
