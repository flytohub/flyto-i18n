#!/usr/bin/env python3
"""
build-dist.py - Build merged locale files for CDN distribution

Usage:
    python scripts/build-dist.py

This script:
1. Merges locale files by scope (cloud, landing, all)
2. Converts flat keys to nested format for vue-i18n compatibility
3. Outputs to dist/{scope}/{locale}.json for efficient CDN loading
4. Generates manifest.json with locale metadata

Scopes:
- dist/cloud/{locale}.json  - cloud.* + modules.* + common.* (flyto-cloud)
- dist/landing/{locale}.json - landing.* + common.* (flyto-landing-page)
- dist/{locale}.json - all translations (admin/full access)
"""

import json
from pathlib import Path
from datetime import datetime

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
DIST_DIR = PROJECT_ROOT / 'dist'

# Define scopes and their file prefixes
SCOPES = {
    'cloud': ['cloud.', 'modules.', 'common.'],
    'landing': ['landing.', 'common.'],
}

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
    'pt': {'name': 'Portuguese', 'native': 'Português', 'region': 'PT'},
    'pt-BR': {'name': 'Portuguese (Brazil)', 'native': 'Português (Brasil)', 'region': 'BR'},
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

    Handles key conflicts:
    - If both "a.b" and "a.b.c" exist, "a.b" is replaced by dict containing "c"
    - Longer/more specific keys always win
    """
    result = {}

    # Sort keys by length descending - longer keys first
    # This ensures children are set before parents try to overwrite
    sorted_keys = sorted(flat_dict.keys(), key=len, reverse=True)

    for key in sorted_keys:
        value = flat_dict[key]

        # Strip "cloud." prefix for cloud keys
        normalized_key = key[6:] if key.startswith('cloud.') else key

        parts = normalized_key.split('.')
        current = result

        # Navigate/create path to parent
        for part in parts[:-1]:
            if part not in current:
                current[part] = {}
            elif not isinstance(current[part], dict):
                # Conflict: shorter key was string, but we need dict for longer key
                # Replace with dict (longer key wins)
                current[part] = {}
            current = current[part]

        # Set final value only if not already a dict (children exist)
        final_key = parts[-1]
        if final_key not in current:
            current[final_key] = value
        # If already exists as dict, skip (children win over parent string)

    return result


def build_locale(locale: str, scope: str = None) -> dict:
    """Build merged translations for a locale.

    Args:
        locale: The locale code (e.g., 'en', 'zh-TW')
        scope: Optional scope to filter files ('cloud', 'landing', or None for all)
    """
    locale_dir = LOCALES_DIR / locale

    if not locale_dir.exists():
        return {}

    flat_merged = {}
    files_count = 0

    # Get file prefixes for scope
    prefixes = SCOPES.get(scope) if scope else None

    for json_file in sorted(locale_dir.glob('*.json')):
        filename = json_file.name

        # Filter by scope if specified
        if prefixes:
            if not any(filename.startswith(p) for p in prefixes):
                continue

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


def count_translated(locale: str, scope: str = None) -> int:
    """Count non-empty translations for a locale."""
    locale_dir = LOCALES_DIR / locale
    count = 0

    # Get file prefixes for scope
    prefixes = SCOPES.get(scope) if scope else None

    for json_file in locale_dir.glob('*.json'):
        filename = json_file.name

        # Filter by scope if specified
        if prefixes:
            if not any(filename.startswith(p) for p in prefixes):
                continue

        with open(json_file, encoding='utf-8') as f:
            data = json.load(f)
        if 'translations' in data:
            count += sum(1 for v in data['translations'].values() if v)

    return count


def main():
    print("Building dist/ for CDN distribution")
    print()

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # Get all locales
    locales = [d.name for d in sorted(LOCALES_DIR.iterdir()) if d.is_dir()]

    # Build scoped files first
    for scope in SCOPES:
        scope_dir = DIST_DIR / scope
        scope_dir.mkdir(parents=True, exist_ok=True)
        print(f"[{scope}]")

        scope_locales_data = {}
        scope_flat_counts = {}

        for locale in locales:
            data = build_locale(locale, scope=scope)
            scope_locales_data[locale] = data
            scope_flat_counts[locale] = count_translated(locale, scope=scope)

            # Write merged file
            output_file = scope_dir / f"{locale}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False)

            print(f"  → dist/{scope}/{locale}.json ({data['total_keys']} keys, {data['files_merged']} files)")

        # Write scope manifest
        manifest = build_manifest(scope_locales_data, scope_flat_counts)
        manifest_file = scope_dir / 'manifest.json'
        with open(manifest_file, 'w', encoding='utf-8') as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)

        print(f"  → dist/{scope}/manifest.json")
        print()

    # Build full (all translations) for admin/full access
    print("[all]")
    all_locales_data = {}
    all_flat_counts = {}

    for locale in locales:
        data = build_locale(locale, scope=None)
        all_locales_data[locale] = data
        all_flat_counts[locale] = count_translated(locale, scope=None)

        # Write merged file
        output_file = DIST_DIR / f"{locale}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        print(f"  → dist/{locale}.json ({data['total_keys']} keys, {data['files_merged']} files)")

    # Write root manifest
    manifest = build_manifest(all_locales_data, all_flat_counts)
    manifest_file = DIST_DIR / 'manifest.json'
    with open(manifest_file, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"  → dist/manifest.json")
    print()
    print("=" * 50)
    print("Build complete!")
    print()

    # Show summary for each scope
    for scope in list(SCOPES.keys()) + ['all']:
        scope_dir = DIST_DIR / scope if scope != 'all' else DIST_DIR
        manifest_file = scope_dir / 'manifest.json'
        if manifest_file.exists():
            with open(manifest_file) as f:
                manifest = json.load(f)
            print(f"[{scope}]")
            for locale, info in manifest['locales'].items():
                status = "✅" if info['completion'] == 100 else "🔄"
                print(f"  {status} {locale}: {info['completion']}% ({info['translated_keys']}/{info['total_keys']})")
            print()


if __name__ == '__main__':
    main()
