#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    'code.footprint.panel.topPaths.loading': ('Counting actionable entities…', '計算可採取行動的實體中…', '统计可采取行动的实体中…', '対応可能なエンティティをカウント中…'),
    'code.footprint.panel.topPaths.summary': ('{n} red-team-actionable entities. The /attack-paths page converges them into the top 5 initial-access hypotheses.', '{n} 個紅隊可採取行動的實體。/attack-paths 頁面會收斂為前 5 大初始入侵假設。', '{n} 个红队可采取行动的实体。/attack-paths 页面会收敛为前 5 大初始入侵假设。', '{n} 件のレッドチーム対応可エンティティ。/attack-paths ページで上位 5 件の初期アクセス仮説に収束します。'),
    'code.footprint.panel.topPaths.viewFull': ('→ View attack paths', '→ 查看攻擊路徑', '→ 查看攻击路径', '→ 攻撃パスを表示'),
}

en_path = ROOT / 'en' / 'code.json'
en = json.loads(en_path.read_text(encoding='utf-8'))
for k, vals in ADDS.items():
    en['translations'][k] = vals[0]
en_path.write_text(json.dumps(en, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'en: +{len(ADDS)}')
for lang_idx, lang in enumerate(('zh-TW', 'zh-CN', 'ja'), start=1):
    p = ROOT / lang / 'code.json'
    doc = json.loads(p.read_text(encoding='utf-8'))
    for k, vals in ADDS.items():
        doc['translations'][k] = vals[lang_idx]
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'{lang}: +{len(ADDS)}')
