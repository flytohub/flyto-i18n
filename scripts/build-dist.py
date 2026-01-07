#!/usr/bin/env python3
"""
build-dist.py - Build merged locale files for CDN distribution

Usage:
    python scripts/build-dist.py

This script:
1. Merges all locale files (modules.*, cloud.*) into single files
2. Outputs to dist/{locale}.json for efficient CDN loading
3. Generates manifest.json with locale metadata
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
DIST_DIR = PROJECT_ROOT / 'dist'


def build_locale(locale: str) -> dict:
    """Build merged translations for a locale."""
    locale_dir = LOCALES_DIR / locale

    if not locale_dir.exists():
        return {}

    merged = {}
    files_count = 0

    for json_file in sorted(locale_dir.glob('*.json')):
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        if 'translations' in data:
            merged.update(data['translations'])
            files_count += 1

    return {
        'locale': locale,
        'version': datetime.now().strftime('%Y%m%d%H%M%S'),
        'files_merged': files_count,
        'total_keys': len(merged),
        'translations': merged
    }


def build_manifest(locales_data: dict) -> dict:
    """Build manifest with locale metadata."""
    manifest = {
        'version': datetime.now().strftime('%Y%m%d%H%M%S'),
        'generated_at': datetime.now().isoformat(),
        'locales': {}
    }

    for locale, data in locales_data.items():
        # Count translated (non-empty) keys
        translated = sum(1 for v in data.get('translations', {}).values() if v)
        total = data.get('total_keys', 0)

        manifest['locales'][locale] = {
            'total_keys': total,
            'translated_keys': translated,
            'completion': round(translated / total * 100, 1) if total > 0 else 0,
            'files_merged': data.get('files_merged', 0)
        }

    return manifest


def main():
    print("Building dist/ for CDN distribution")
    print()

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    locales_data = {}

    # Process each locale
    for locale_dir in sorted(LOCALES_DIR.iterdir()):
        if not locale_dir.is_dir():
            continue

        locale = locale_dir.name
        print(f"[{locale}]")

        data = build_locale(locale)
        locales_data[locale] = data

        # Write merged file
        output_file = DIST_DIR / f"{locale}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        print(f"  → dist/{locale}.json ({data['total_keys']} keys, {data['files_merged']} files)")

    # Write manifest
    manifest = build_manifest(locales_data)
    manifest_file = DIST_DIR / 'manifest.json'
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print()
    print(f"  → dist/manifest.json")
    print()
    print("=" * 50)
    print("Build complete!")
    print()

    # Show summary
    for locale, info in manifest['locales'].items():
        status = "✅" if info['completion'] == 100 else "🔄"
        print(f"  {status} {locale}: {info['completion']}% ({info['translated_keys']}/{info['total_keys']})")


if __name__ == '__main__':
    main()
