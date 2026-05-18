#!/usr/bin/env python3
# fill-zh-cn-gaps.py — one-off, append-only gap filler.
# For every key in en/code.json that is missing or empty in
# zh-CN/code.json, take the zh-TW value, run it through OpenCC
# tw2sp + the project's vocab fixes, and insert it. Existing
# non-empty zh-CN values are NEVER overwritten.

import json
import sys
from pathlib import Path

import opencc

PROJECT_ROOT = Path(__file__).parent.parent.parent
LOCALES = PROJECT_ROOT / 'locales'

# Mirror convert-tw-to-cn.py vocab fixes
TW_TO_CN_VOCAB = [
    ('自订', '自定义'),
    ('范本', '模板'),
    ('网路', '网络'),
    ('帐号', '账号'),
    ('帐户', '账户'),
]


def fix(text: str) -> str:
    for tw, cn in TW_TO_CN_VOCAB:
        text = text.replace(tw, cn)
    return text


def fill(project: str) -> int:
    en_path = LOCALES / project / 'en' / f'{project}.json'
    tw_path = LOCALES / project / 'zh-TW' / f'{project}.json'
    cn_path = LOCALES / project / 'zh-CN' / f'{project}.json'

    en = json.loads(en_path.read_text(encoding='utf-8'))['translations']
    tw = json.loads(tw_path.read_text(encoding='utf-8'))['translations']
    cn_doc = json.loads(cn_path.read_text(encoding='utf-8'))
    cn = cn_doc['translations']

    cc = opencc.OpenCC('tw2sp')

    added = 0
    for key in en:
        if cn.get(key):  # non-empty existing — skip
            continue
        tw_val = tw.get(key)
        if not tw_val:  # zh-TW also missing — can't backfill
            continue
        cn[key] = fix(cc.convert(tw_val))
        added += 1

    if added:
        cn_doc['translations'] = cn
        cn_path.write_text(
            json.dumps(cn_doc, indent=2, ensure_ascii=False) + '\n',
            encoding='utf-8',
        )
    return added


if __name__ == '__main__':
    project = sys.argv[1] if len(sys.argv) > 1 else 'code'
    n = fill(project)
    print(f'{project}: filled {n} zh-CN keys from zh-TW')
