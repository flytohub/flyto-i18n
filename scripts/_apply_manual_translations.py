#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    # VendorRiskView risk tones
    'code.vendors.riskTone.critical': ('Critical', '嚴重', '严重', '重大'),
    'code.vendors.riskTone.high': ('High', '高', '高', '高'),
    'code.vendors.riskTone.medium': ('Medium', '中', '中', '中'),
    'code.vendors.riskTone.low': ('Low', '低', '低', '低'),
    'code.vendors.riskTone.unknown': ('Not assessed', '未評估', '未评估', '未評価'),
    # ScanningTab cadences
    'code.settings.scanning.cadence.daily': ('Daily', '每日', '每日', '毎日'),
    'code.settings.scanning.cadence.weekly': ('Weekly (recommended)', '每週(建議)', '每周(建议)', '週次 (推奨)'),
    'code.settings.scanning.cadence.manual': ('Manual only', '僅手動', '仅手动', '手動のみ'),
    'code.settings.scanning.cadence.daily_full': ('Daily + DAST', '每日 + DAST', '每日 + DAST', '毎日 + DAST'),
    # ScanLogTab statuses
    'code.settings.scanLog.status.complete': ('Complete', '完成', '完成', '完了'),
    'code.settings.scanLog.status.failed': ('Failed', '失敗', '失败', '失敗'),
    'code.settings.scanLog.status.running': ('Running', '執行中', '执行中', '実行中'),
    'code.settings.scanLog.status.queued': ('Queued', '已排程', '已排程', 'キュー'),
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
