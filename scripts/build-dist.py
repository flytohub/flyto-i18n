#!/usr/bin/env python3
"""
build-dist.py - Build merged locale files for CDN distribution

Usage:
    python scripts/build-dist.py

This script:
1. Merges all locale files (modules.*, cloud.*) into single files
2. Converts flat keys to nested format for vue-i18n compatibility
3. Outputs to dist/{locale}.json for efficient CDN loading
4. Generates manifest.json with locale metadata
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
DIST_DIR = PROJECT_ROOT / 'dist'

# Language metadata - add new languages here when adding locales
LANGUAGE_META = {
    'en': {'name': 'English', 'native': 'English', 'region': 'US'},
    'zh-TW': {'name': 'Traditional Chinese', 'native': '繁體中文', 'region': 'TW'},
    'zh-CN': {'name': 'Simplified Chinese', 'native': '简体中文', 'region': 'CN'},
    'ja': {'name': 'Japanese', 'native': '日本語', 'region': 'JP'},
    'ko': {'name': 'Korean', 'native': '한국어', 'region': 'KR'},
    'es': {'name': 'Spanish', 'native': 'Español', 'region': 'ES'},
    'fr': {'name': 'French', 'native': 'Français', 'region': 'FR'},
    'de': {'name': 'German', 'native': 'Deutsch', 'region': 'DE'},
    'pt': {'name': 'Portuguese', 'native': 'Português', 'region': 'BR'},
    'it': {'name': 'Italian', 'native': 'Italiano', 'region': 'IT'},
    'ru': {'name': 'Russian', 'native': 'Русский', 'region': 'RU'},
    'th': {'name': 'Thai', 'native': 'ไทย', 'region': 'TH'},
    'vi': {'name': 'Vietnamese', 'native': 'Tiếng Việt', 'region': 'VN'},
    'ar': {'name': 'Arabic', 'native': 'العربية', 'region': 'SA'},
    'hi': {'name': 'Hindi', 'native': 'हिन्दी', 'region': 'IN'},
    'id': {'name': 'Indonesian', 'native': 'Bahasa Indonesia', 'region': 'ID'},
    'ms': {'name': 'Malay', 'native': 'Bahasa Melayu', 'region': 'MY'},
    'nl': {'name': 'Dutch', 'native': 'Nederlands', 'region': 'NL'},
    'pl': {'name': 'Polish', 'native': 'Polski', 'region': 'PL'},
    'tr': {'name': 'Turkish', 'native': 'Türkçe', 'region': 'TR'},
    'uk': {'name': 'Ukrainian', 'native': 'Українська', 'region': 'UA'},
}


def flat_to_nested(flat_dict: dict) -> dict:
    """
    Convert flat keys to nested object for vue-i18n compatibility.

    "cloud.myTemplates.title" → { myTemplates: { title: "..." } }
    "modules.browser.click.label" → { modules: { browser: { click: { label: "..." } } } }

    Strips "cloud." prefix so t('myTemplates.title') works directly.
    """
    result = {}

    for key, value in flat_dict.items():
        # Strip "cloud." prefix for cloud keys
        normalized_key = key[6:] if key.startswith('cloud.') else key

        # Split key and build nested structure
        parts = normalized_key.split('.')
        current = result

        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            elif not isinstance(current[part], dict):
                # Handle conflict: existing value is not a dict
                current[part] = {'_value': current[part]}
            current = current[part]

        # Set the final value
        final_key = parts[-1]
        if final_key in current and isinstance(current[final_key], dict):
            current[final_key]['_value'] = value
        else:
            current[final_key] = value

    return result


def build_locale(locale: str) -> dict:
    """Build merged translations for a locale."""
    locale_dir = LOCALES_DIR / locale

    if not locale_dir.exists():
        return {}

    flat_merged = {}
    files_count = 0

    for json_file in sorted(locale_dir.glob('*.json')):
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)

        if 'translations' in data:
            flat_merged.update(data['translations'])
            files_count += 1

    # Convert to nested format
    nested = flat_to_nested(flat_merged)

    # Get language metadata
    meta = LANGUAGE_META.get(locale, {'name': locale, 'native': locale, 'region': locale[:2].upper()})

    return {
        'locale': locale,
        'name': meta['name'],
        'native': meta['native'],
        'region': meta['region'],
        'version': datetime.now().strftime('%Y%m%d%H%M%S'),
        'files_merged': files_count,
        'total_keys': len(flat_merged),
        'translations': nested
    }


def build_manifest(locales_data: dict, flat_counts: dict) -> dict:
    """Build manifest with locale metadata."""
    manifest = {
        'version': datetime.now().strftime('%Y%m%d%H%M%S'),
        'generated_at': datetime.now().isoformat(),
        'locales': {}
    }

    for locale, data in locales_data.items():
        total = data.get('total_keys', 0)
        # Use flat count for accurate translated count
        translated = flat_counts.get(locale, 0)

        # Get language metadata
        meta = LANGUAGE_META.get(locale, {'name': locale, 'native': locale, 'region': locale[:2].upper()})

        manifest['locales'][locale] = {
            'name': meta['name'],
            'native': meta['native'],
            'region': meta['region'],
            'total_keys': total,
            'translated_keys': translated,
            'completion': round(translated / total * 100, 1) if total > 0 else 0,
            'files_merged': data.get('files_merged', 0)
        }

    return manifest


def count_translated(locale: str) -> int:
    """Count non-empty translations for a locale."""
    locale_dir = LOCALES_DIR / locale
    count = 0

    for json_file in locale_dir.glob('*.json'):
        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
        if 'translations' in data:
            count += sum(1 for v in data['translations'].values() if v)

    return count


def main():
    print("Building dist/ for CDN distribution")
    print()

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    locales_data = {}
    flat_counts = {}

    # Process each locale
    for locale_dir in sorted(LOCALES_DIR.iterdir()):
        if not locale_dir.is_dir():
            continue

        locale = locale_dir.name
        print(f"[{locale}]")

        data = build_locale(locale)
        locales_data[locale] = data
        flat_counts[locale] = count_translated(locale)

        # Write merged file
        output_file = DIST_DIR / f"{locale}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        print(f"  → dist/{locale}.json ({data['total_keys']} keys, {data['files_merged']} files)")

    # Write manifest
    manifest = build_manifest(locales_data, flat_counts)
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
