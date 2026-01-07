#!/usr/bin/env python3
"""
sync-locales.py - Sync all locales with English base

Usage:
    python scripts/sync-locales.py [--dry-run]

This script:
1. Scans English (base) locale for all keys
2. For each other locale:
   - Adds missing keys (with empty value)
   - Removes keys that don't exist in English
3. Maintains the same file structure as English
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, Set

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
EN_DIR = LOCALES_DIR / 'en'


def load_locale_keys(locale_dir: Path) -> Dict[str, Dict[str, str]]:
    """Load all keys from a locale directory, grouped by file."""
    result = {}

    for json_file in locale_dir.glob('*.json'):
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        if 'translations' in data:
            result[json_file.name] = data['translations']

    return result


def sync_locale(locale: str, dry_run: bool = False) -> Dict[str, int]:
    """Sync a locale with English base."""
    locale_dir = LOCALES_DIR / locale
    stats = {'added': 0, 'removed': 0, 'files_updated': 0}

    if not locale_dir.exists():
        print(f"  Warning: Locale directory not found: {locale_dir}")
        return stats

    # Load English keys
    en_keys = load_locale_keys(EN_DIR)

    for en_file in sorted(EN_DIR.glob('*.json')):
        filename = en_file.name
        target_file = locale_dir / filename

        # Load English data
        with open(en_file, encoding='utf-8') as f:
            en_data = json.load(f)

        en_translations = en_data.get('translations', {})

        # Load or create target locale data
        if target_file.exists():
            with open(target_file, encoding='utf-8') as f:
                target_data = json.load(f)
            target_translations = target_data.get('translations', {})
        else:
            # Create new file based on English structure
            target_data = en_data.copy()
            target_data['locale'] = locale
            target_translations = {}

        # Calculate changes
        en_key_set = set(en_translations.keys())
        target_key_set = set(target_translations.keys())

        keys_to_add = en_key_set - target_key_set
        keys_to_remove = target_key_set - en_key_set

        if not keys_to_add and not keys_to_remove:
            continue

        # Apply changes
        new_translations = {}

        # Keep existing translations for keys that exist in English
        for key in en_translations.keys():
            if key in target_translations:
                new_translations[key] = target_translations[key]
            else:
                new_translations[key] = ""  # New key, empty value
                stats['added'] += 1

        stats['removed'] += len(keys_to_remove)
        stats['files_updated'] += 1

        # Update target data
        target_data['translations'] = dict(sorted(new_translations.items()))
        target_data['locale'] = locale

        change_info = []
        if keys_to_add:
            change_info.append(f"+{len(keys_to_add)}")
        if keys_to_remove:
            change_info.append(f"-{len(keys_to_remove)}")

        if dry_run:
            print(f"  Would update {filename}: {', '.join(change_info)}")
        else:
            with open(target_file, 'w', encoding='utf-8') as f:
                json.dump(target_data, f, indent=2, ensure_ascii=False)
            print(f"  Updated {filename}: {', '.join(change_info)}")

    return stats


def main():
    parser = argparse.ArgumentParser(description='Sync all locales with English')
    parser.add_argument('--dry-run', action='store_true', help='Show changes without applying')
    parser.add_argument('--locale', '-l', help='Sync specific locale only')
    args = parser.parse_args()

    print("Syncing locales with English base")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()

    total_stats = {'added': 0, 'removed': 0, 'files_updated': 0}

    # Get all locales except English
    if args.locale:
        locales = [args.locale]
    else:
        locales = [d.name for d in LOCALES_DIR.iterdir()
                   if d.is_dir() and d.name != 'en']

    for locale in sorted(locales):
        print(f"[{locale}]")
        stats = sync_locale(locale, dry_run=args.dry_run)

        if stats['files_updated'] == 0:
            print("  Already in sync ✓")

        total_stats['added'] += stats['added']
        total_stats['removed'] += stats['removed']
        total_stats['files_updated'] += stats['files_updated']
        print()

    print("=" * 50)
    print(f"Summary:")
    print(f"  Keys added:   +{total_stats['added']}")
    print(f"  Keys removed: -{total_stats['removed']}")
    print(f"  Files updated: {total_stats['files_updated']}")
    print("=" * 50)

    if args.dry_run:
        print("\nRun without --dry-run to apply changes")


if __name__ == '__main__':
    main()
