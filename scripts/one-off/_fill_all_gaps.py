#!/usr/bin/env python3
"""Fill ALL empty translation values across all locales.

Strategy:
1. en empty → generate from key name
2. zh-TW empty → copy en value (will need manual review for quality)
3. All other locales empty → copy en value (so fallback shows English, not blank)
"""
import json
import re
from pathlib import Path

LOCALES_DIR = Path(__file__).parent.parent / 'locales'

def key_to_english(key):
    """Generate English text from a translation key name."""
    parts = key.split('.')
    # Use last meaningful segment(s)
    if len(parts) >= 3:
        last = parts[-1]
        parent = parts[-2]
    elif len(parts) >= 2:
        last = parts[-1]
        parent = parts[-2] if parts[-2] not in ('cloud', 'code', 'landing', 'modules', 'shared', 'app', 'console', 'data') else ''
    else:
        last = parts[-1]
        parent = ''

    # camelCase to words
    words = re.sub(r'([a-z])([A-Z])', r'\1 \2', last)
    words = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', words)
    result = words[0].upper() + words[1:] if words else last
    return result


def get_en_value(scope, key):
    """Get English value for a key from the en locale file."""
    # Find which file has this key
    en_dir = LOCALES_DIR / scope / 'en'
    for f in en_dir.rglob('*.json'):
        with open(f, encoding='utf-8') as fh:
            data = json.load(fh)
        if key in data.get('translations', {}):
            val = data['translations'][key]
            if val:
                return val
    return None


# Cache en values per scope
en_cache = {}

def load_en_cache(scope):
    if scope in en_cache:
        return en_cache[scope]
    en_dir = LOCALES_DIR / scope / 'en'
    cache = {}
    for f in sorted(en_dir.rglob('*.json')):
        with open(f, encoding='utf-8') as fh:
            data = json.load(fh)
        for k, v in data.get('translations', {}).items():
            if v:
                cache[k] = v
    en_cache[scope] = cache
    return cache


def fill_scope(scope):
    total_filled = 0
    en_vals = load_en_cache(scope)

    for locale_dir in sorted((LOCALES_DIR / scope).iterdir()):
        if not locale_dir.is_dir():
            continue
        locale = locale_dir.name

        for f in sorted(locale_dir.rglob('*.json')):
            with open(f, encoding='utf-8') as fh:
                data = json.load(fh)

            translations = data.get('translations', {})
            filled = 0

            for k, v in translations.items():
                if v != '':
                    continue

                if locale == 'en':
                    # Generate from key name
                    translations[k] = key_to_english(k)
                    filled += 1
                else:
                    # Copy from English
                    en_val = en_vals.get(k)
                    if en_val:
                        translations[k] = en_val
                        filled += 1
                    else:
                        # en is also empty, generate
                        translations[k] = key_to_english(k)
                        filled += 1

            if filled > 0:
                data['translations'] = translations
                with open(f, 'w', encoding='utf-8') as fh:
                    json.dump(data, fh, indent=2, ensure_ascii=False)
                    fh.write('\n')
                total_filled += filled

        if total_filled > 0:
            pass  # quiet per-locale output

    return total_filled


def main():
    grand_total = 0
    for scope in ['cloud', 'code', 'landing', 'app', 'console', 'data']:
        filled = fill_scope(scope)
        if filled > 0:
            print(f'  {scope}: filled {filled} empty values')
            grand_total += filled

    print(f'\nTotal filled: {grand_total}')

    # Verify zero remaining
    remaining = 0
    for scope in ['cloud', 'code', 'landing', 'app', 'console', 'data']:
        for f in (LOCALES_DIR / scope).rglob('*.json'):
            with open(f, encoding='utf-8') as fh:
                data = json.load(fh)
            for v in data.get('translations', {}).values():
                if v == '':
                    remaining += 1

    print(f'Remaining empty: {remaining}')


if __name__ == '__main__':
    main()
