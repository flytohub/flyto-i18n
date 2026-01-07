#!/usr/bin/env python3
"""
add-locale.py - Add a new locale based on English

Usage:
    python scripts/add-locale.py ja          # Add Japanese
    python scripts/add-locale.py ko          # Add Korean
    python scripts/add-locale.py --list      # List available locales

This script:
1. Creates new locale directory
2. Copies all English files with empty values (or English as placeholder)
3. Maintains the same structure as English base
"""

import argparse
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
EN_DIR = LOCALES_DIR / 'en'

# Common locale codes
LOCALE_NAMES = {
    'en': 'English',
    'zh-TW': 'Traditional Chinese',
    'zh-CN': 'Simplified Chinese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'pt': 'Portuguese',
    'it': 'Italian',
    'ru': 'Russian',
    'ar': 'Arabic',
    'th': 'Thai',
    'vi': 'Vietnamese',
}


def empty_values(obj):
    """Recursively set all string values to empty."""
    if isinstance(obj, dict):
        return {k: empty_values(v) for k, v in obj.items()}
    elif isinstance(obj, str):
        return ""
    else:
        return obj


def add_locale(locale: str, use_english_values: bool = False):
    """Add a new locale based on English."""
    target_dir = LOCALES_DIR / locale

    if target_dir.exists():
        print(f"Locale '{locale}' already exists at {target_dir}")
        return False

    if not EN_DIR.exists():
        print(f"Error: English base locale not found at {EN_DIR}")
        return False

    target_dir.mkdir(parents=True, exist_ok=True)

    files_created = 0
    total_keys = 0

    for en_file in sorted(EN_DIR.glob('*.json')):
        with open(en_file, encoding='utf-8') as f:
            data = json.load(f)

        # Update locale field
        data['locale'] = locale

        # Process translations
        if 'translations' in data:
            if use_english_values:
                # Keep English values as placeholders
                pass
            else:
                # Set all values to empty strings
                data['translations'] = {k: "" for k in data['translations'].keys()}

            total_keys += len(data['translations'])

        # Write to new locale
        target_file = target_dir / en_file.name
        with open(target_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        files_created += 1
        print(f"  Created {target_file.name}")

    print()
    print(f"✅ Locale '{locale}' created successfully!")
    print(f"   Files: {files_created}")
    print(f"   Keys: {total_keys} (empty)")
    print()
    print(f"Next steps:")
    print(f"  1. Translate the files in locales/{locale}/")
    print(f"  2. Run: python scripts/sync-locales.py")
    print(f"  3. Commit and push")

    return True


def list_locales():
    """List all available locales."""
    print("Available locales:")
    print()

    for locale_dir in sorted(LOCALES_DIR.iterdir()):
        if locale_dir.is_dir():
            files = list(locale_dir.glob('*.json'))
            keys = 0
            translated = 0

            for f in files:
                with open(f, encoding='utf-8') as fp:
                    data = json.load(fp)
                    if 'translations' in data:
                        for v in data['translations'].values():
                            keys += 1
                            if v:  # Non-empty
                                translated += 1

            pct = (translated / keys * 100) if keys > 0 else 0
            name = LOCALE_NAMES.get(locale_dir.name, '')
            status = "✅" if pct == 100 else "🔄" if pct > 0 else "⬜"

            print(f"  {status} {locale_dir.name:8} {name:25} {translated:5}/{keys:5} ({pct:.1f}%)")

    print()
    print("To add a new locale: python scripts/add-locale.py <locale_code>")


def main():
    parser = argparse.ArgumentParser(description='Add a new locale')
    parser.add_argument('locale', nargs='?', help='Locale code (e.g., ja, ko, es)')
    parser.add_argument('--list', '-l', action='store_true', help='List available locales')
    parser.add_argument('--with-english', '-e', action='store_true',
                        help='Use English values as placeholders instead of empty strings')
    args = parser.parse_args()

    if args.list or not args.locale:
        list_locales()
        return

    locale = args.locale
    print(f"Adding new locale: {locale}")
    if locale in LOCALE_NAMES:
        print(f"Language: {LOCALE_NAMES[locale]}")
    print()

    add_locale(locale, use_english_values=args.with_english)


if __name__ == '__main__':
    main()
