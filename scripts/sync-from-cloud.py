#!/usr/bin/env python3
"""
sync-from-cloud.py - Sync i18n keys from flyto-cloud

This script copies UI translations from flyto-cloud to flyto-i18n,
converting nested JSON structure to flat keys with 'cloud.' prefix.

Usage:
    python scripts/sync-from-cloud.py [--cloud-path PATH] [--dry-run]

Options:
    --cloud-path    Path to flyto-cloud (default: ../flyto-cloud)
    --dry-run       Show changes without writing files
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'


def flatten_dict(d: Dict[str, Any], parent_key: str = '', sep: str = '.') -> Dict[str, str]:
    """Flatten nested dictionary to dot-separated keys."""
    items = []
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.extend(flatten_dict(v, new_key, sep).items())
        else:
            items.append((new_key, str(v)))
    return dict(items)


def sync_locale(cloud_path: Path, locale: str, dry_run: bool = False) -> Dict[str, int]:
    """Sync translations for a specific locale."""
    cloud_i18n_dir = cloud_path / 'src' / 'ui' / 'web' / 'frontend' / 'src' / 'i18n' / 'locales' / locale
    target_dir = LOCALES_DIR / locale

    stats = {'files': 0, 'keys': 0, 'new_keys': 0}

    if not cloud_i18n_dir.exists():
        print(f"  Warning: Cloud locale directory not found: {cloud_i18n_dir}")
        return stats

    target_dir.mkdir(parents=True, exist_ok=True)

    for json_file in sorted(cloud_i18n_dir.glob('*.json')):
        category = json_file.stem  # e.g., 'auth', 'dashboard'

        try:
            with open(json_file, encoding='utf-8') as f:
                data = json.load(f)
        except Exception as e:
            print(f"  Warning: Could not read {json_file}: {e}")
            continue

        # Flatten nested structure and add 'cloud.' prefix
        flat_translations = {}
        for key, value in flatten_dict(data).items():
            # Add 'cloud.' prefix to distinguish from module translations
            flat_key = f"cloud.{key}"
            flat_translations[flat_key] = value

        if not flat_translations:
            continue

        # Target filename: cloud.{category}.json
        target_file = target_dir / f"cloud.{category}.json"

        # Load existing keys to calculate diff
        existing_keys = set()
        if target_file.exists():
            try:
                with open(target_file, encoding='utf-8') as f:
                    existing_data = json.load(f)
                    existing_keys = set(existing_data.get('translations', {}).keys())
            except:
                pass

        new_keys = set(flat_translations.keys()) - existing_keys

        # Create output structure matching flyto-i18n schema
        output = {
            "$schema": "../../schema/locale.schema.json",
            "locale": locale,
            "category": f"cloud.{category}",
            "version": "1.0.0",
            "translations": dict(sorted(flat_translations.items()))
        }

        stats['files'] += 1
        stats['keys'] += len(flat_translations)
        stats['new_keys'] += len(new_keys)

        change_info = f" (+{len(new_keys)} new)" if new_keys else ""

        if dry_run:
            print(f"  Would write {target_file.name}: {len(flat_translations)} keys{change_info}")
        else:
            with open(target_file, 'w', encoding='utf-8') as f:
                json.dump(output, f, indent=2, ensure_ascii=False)
            print(f"  Wrote {target_file.name}: {len(flat_translations)} keys{change_info}")

    return stats


def main():
    parser = argparse.ArgumentParser(description='Sync keys from flyto-cloud')
    parser.add_argument('--cloud-path', default='../flyto-cloud',
                        help='Path to flyto-cloud')
    parser.add_argument('--dry-run', action='store_true',
                        help='Show changes without writing')
    args = parser.parse_args()

    cloud_path = Path(args.cloud_path).resolve()
    if not cloud_path.exists():
        print(f"Error: flyto-cloud not found at {cloud_path}")
        sys.exit(1)

    print(f"Syncing from flyto-cloud at: {cloud_path}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE'}")
    print()

    total_stats = {'files': 0, 'keys': 0, 'new_keys': 0}

    # Sync each locale
    for locale in ['en', 'zh-TW']:
        print(f"[{locale}]")
        stats = sync_locale(cloud_path, locale, args.dry_run)
        total_stats['files'] += stats['files']
        total_stats['keys'] += stats['keys']
        total_stats['new_keys'] += stats['new_keys']
        print()

    print("=" * 50)
    print(f"Summary:")
    print(f"  Files: {total_stats['files']}")
    print(f"  Total keys: {total_stats['keys']}")
    print(f"  New keys: +{total_stats['new_keys']}")
    print("=" * 50)

    if args.dry_run:
        print("\nRun without --dry-run to apply changes")


if __name__ == '__main__':
    main()
