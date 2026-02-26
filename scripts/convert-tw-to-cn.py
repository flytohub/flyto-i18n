#!/usr/bin/env python3
"""
convert-tw-to-cn.py - Convert zh-TW locale to zh-CN using OpenCC

Usage:
    python scripts/convert-tw-to-cn.py
    python scripts/convert-tw-to-cn.py --dry-run

Uses OpenCC tw2sp profile which handles:
- Traditional → Simplified character conversion
- Taiwan → Mainland vocabulary conversion (檔案→文件, 軟體→软件, etc.)

Requirements:
    pip install opencc-python-reimplemented
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import opencc
except ImportError:
    print("Error: opencc not installed")
    print("Run: pip install opencc-python-reimplemented")
    sys.exit(1)

PROJECT_ROOT = Path(__file__).parent.parent
LOCALES_DIR = PROJECT_ROOT / 'locales'
TW_DIR = LOCALES_DIR / 'zh-TW'
CN_DIR = LOCALES_DIR / 'zh-CN'


def convert_value(cc: opencc.OpenCC, value):
    """Recursively convert string values."""
    if isinstance(value, str):
        return cc.convert(value)
    elif isinstance(value, dict):
        return {k: convert_value(cc, v) for k, v in value.items()}
    elif isinstance(value, list):
        return [convert_value(cc, item) for item in value]
    return value


def main():
    parser = argparse.ArgumentParser(description='Convert zh-TW to zh-CN using OpenCC')
    parser.add_argument('--dry-run', action='store_true', help='Preview without writing')
    parser.add_argument('--force', action='store_true', help='Overwrite existing zh-CN files')
    args = parser.parse_args()

    cc = opencc.OpenCC('tw2sp')

    if not TW_DIR.exists():
        print(f"Error: zh-TW directory not found at {TW_DIR}")
        sys.exit(1)

    if not args.dry_run:
        CN_DIR.mkdir(parents=True, exist_ok=True)

    tw_files = sorted(TW_DIR.glob('*.json'))
    print(f"Converting {len(tw_files)} files from zh-TW → zh-CN")
    print(f"Mode: {'DRY RUN' if args.dry_run else ('FORCE' if args.force else 'NORMAL')}")
    print()

    converted = 0
    skipped = 0

    for tw_file in tw_files:
        cn_file = CN_DIR / tw_file.name

        if cn_file.exists() and not args.force:
            print(f"  SKIP {tw_file.name} (already exists)")
            skipped += 1
            continue

        with open(tw_file, encoding='utf-8') as f:
            data = json.load(f)

        # Update locale field
        data['locale'] = 'zh-CN'

        # Convert translations
        if 'translations' in data:
            data['translations'] = {
                k: cc.convert(v) if isinstance(v, str) else v
                for k, v in data['translations'].items()
            }

        if args.dry_run:
            # Show a few sample conversions
            if 'translations' in data:
                samples = list(data['translations'].items())[:3]
                for k, v in samples:
                    with open(tw_file, encoding='utf-8') as f:
                        orig = json.load(f)['translations'].get(k, '')
                    if orig != v:
                        print(f"  {tw_file.name}: {k}")
                        print(f"    TW: {orig}")
                        print(f"    CN: {v}")
            print(f"  WOULD convert {tw_file.name}")
        else:
            with open(cn_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
                f.write('\n')
            print(f"  OK {tw_file.name}")

        converted += 1

    print()
    print(f"Done: {converted} converted, {skipped} skipped")


if __name__ == '__main__':
    main()
