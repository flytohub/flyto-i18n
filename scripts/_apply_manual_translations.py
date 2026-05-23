#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    # AutofixPreviewModal steps
    'code.autofix.previewStep.clone': ('Cloning repository at the latest scanned commit', '從最近掃描的 commit 複製儲存庫', '从最近扫描的 commit 复制仓库', '最新スキャン済コミットからリポジトリをクローン'),
    'code.autofix.previewStep.detect': ('Locating the vulnerability in the working tree', '在工作樹中定位漏洞', '在工作树中定位漏洞', '作業ツリー内で脆弱性を特定'),
    'code.autofix.previewStep.transform': ('Generating the patch', '產生修補', '生成补丁', 'パッチ生成中'),
    'code.autofix.previewStep.verify': ('Running verify gates (lint, build, test)', '執行驗證閘門(lint、build、test)', '执行验证闸门(lint、build、test)', '検証ゲートを実行 (lint、build、test)'),
    'code.autofix.previewStep.persist': ('Caching preview so the diff opens instantly next time', '快取預覽以便下次立即開啟差異', '缓存预览以便下次立即打开差异', 'プレビューをキャッシュして次回 diff が即時オープン'),
    # VendorFormDialog categories
    'code.vendors.category.cdn': ('CDN', 'CDN', 'CDN', 'CDN'),
    'code.vendors.category.hosting': ('Hosting', '託管', '托管', 'ホスティング'),
    'code.vendors.category.analytics': ('Analytics', '分析', '分析', '分析'),
    'code.vendors.category.payment': ('Payment', '支付', '支付', '決済'),
    'code.vendors.category.saas': ('SaaS', 'SaaS', 'SaaS', 'SaaS'),
    'code.vendors.category.other': ('Other', '其他', '其他', 'その他'),
    # BudgetPoliciesTab
    'code.settings.budget.hardStop': ('Hard Stop', '硬停止', '硬停止', 'ハードストップ'),
    'code.settings.budget.active': ('Active', '啟用中', '启用中', 'アクティブ'),
    'code.settings.budget.inactive': ('Inactive', '已停用', '已停用', '非アクティブ'),
    'code.settings.budget.metricTotal': ('Total Tokens', '總 token', '总 token', '合計トークン'),
    'code.settings.budget.metricInput': ('Input Tokens', '輸入 token', '输入 token', '入力トークン'),
    'code.settings.budget.metricOutput': ('Output Tokens', '輸出 token', '输出 token', '出力トークン'),
    'code.settings.budget.amountPlaceholder': ('Amount', '數量', '数量', '数量'),
    'code.settings.budget.window1d': ('1 day', '1 天', '1 天', '1 日'),
    'code.settings.budget.window7d': ('7 days', '7 天', '7 天', '7 日'),
    'code.settings.budget.window30d': ('30 days', '30 天', '30 天', '30 日'),
    'code.settings.budget.warnPercentPlaceholder': ('Warn %', '警示 %', '警示 %', '警告 %'),
    # AssetMapView
    'code.assetMap.selectRepoAria': ('Select repo', '選擇儲存庫', '选择仓库', 'リポジトリを選択'),
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
