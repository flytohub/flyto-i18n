#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    # ComplianceDashboardView
    'code.compliance.overall': ('Overall', '整體', '整体', '全体'),
    # PostureOverview
    'code.posture.clearSelection': ('Clear selection', '清除選擇', '清除选择', '選択を解除'),
    'code.posture.sectorBand.top5': ('Top 5%', '前 5%', '前 5%', '上位 5%'),
    'code.posture.sectorBand.top10': ('Top 10%', '前 10%', '前 10%', '上位 10%'),
    'code.posture.sectorBand.top25': ('Top 25%', '前 25%', '前 25%', '上位 25%'),
    'code.posture.sectorBand.aboveP50': ('Above sector P50', '高於產業 P50', '高于行业 P50', '業界 P50 以上'),
    'code.posture.sectorBand.bottom50': ('Bottom 50%', '後 50%', '后 50%', '下位 50%'),
    'code.posture.sectorBand.bottom25': ('Bottom 25%', '後 25%', '后 25%', '下位 25%'),
    # IssuesSidebar
    'code.issues.category.all': ('All Findings', '所有發現項', '所有发现项', 'すべての検出'),
    'code.issues.category.cve': ('Vulnerabilities', '漏洞', '漏洞', '脆弱性'),
    'code.issues.category.secret': ('Exposed Secrets', '已曝露的機密', '已暴露的密钥', '露出シークレット'),
    'code.issues.category.security_finding': ('Code Issues', '程式碼問題', '代码问题', 'コード問題'),
    # HistoryTimeline
    'code.history.event.created': ('Alert created', '警示已建立', '警示已创建', 'アラート作成'),
    'code.history.event.statusPrefix': ('Status', '狀態', '状态', '状態'),
    'code.history.event.resolved': ('Resolved', '已解決', '已解决', '解決済'),
    'code.history.event.resolvedBadge': ('resolved', '已解決', '已解决', '解決済'),
    'code.history.event.reopened': ('Reopened', '重新開啟', '重新打开', '再オープン'),
    'code.history.event.assignedTo': ('Assigned to', '指派給', '分配给', '担当者'),
    'code.history.event.snoozed': ('Snoozed', '已延後', '已延后', 'スヌーズ'),
    # ScoringMethodology dimensions
    'code.scoringMethod.dim.security': ('Security', '安全性', '安全性', 'セキュリティ'),
    'code.scoringMethod.dim.complexity': ('Complexity', '複雜度', '复杂度', '複雑度'),
    'code.scoringMethod.dim.docs': ('Docs', '文件', '文档', 'ドキュメント'),
    'code.scoringMethod.dim.deadCode': ('Dead Code', '無用程式碼', '无用代码', 'デッドコード'),
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
