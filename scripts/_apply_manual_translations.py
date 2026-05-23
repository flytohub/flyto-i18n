#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    'code.footprint.claim.seed_links_to_entity': ('Seed website links to entity', '種子網站連到此實體', '种子网站链接到此实体', 'シードサイトから当エンティティへリンク'),
    'code.footprint.claim.entity_links_back_to_seed': ('Entity links back to seed', '實體連回種子', '实体链接回种子', 'エンティティがシードに逆リンク'),
    'code.footprint.claim.entity_mentions_seed_domain': ('Mentions seed domain', '提及種子網域', '提及种子域名', 'シードドメインを言及'),
    'code.footprint.claim.ssl_san_includes': ('SSL SAN includes', 'SSL SAN 包含', 'SSL SAN 包含', 'SSL SAN に含む'),
    'code.footprint.claim.subdomain_of_seed_domain': ('Subdomain of seed (CT log)', '種子的子網域(CT log)', '种子的子域名(CT log)', 'シードのサブドメイン (CT log)'),
    'code.footprint.claim.email_domain_matches_seed': ('Email domain matches seed', '電郵網域與種子相符', '邮件域名与种子相符', 'メールドメインがシードと一致'),
    'code.footprint.claim.mx_resolves': ('MX record resolves', 'MX 記錄可解析', 'MX 记录可解析', 'MX レコードが解決'),
    'code.footprint.claim.canonical_metadata': ('Authoritative metadata', '權威來源詮釋資料', '权威来源元数据', '権威メタデータ'),
    'code.footprint.claim.desc_brand_plus_domain': ('Description: brand + domain', '描述含品牌+網域', '描述含品牌+域名', '説明にブランド+ドメイン'),
    'code.footprint.claim.alias_co_mention': ('Alias co-mention (alias graph)', '別名共同提及', '别名共同提及', 'エイリアス共起'),
    'code.footprint.claim.name_high_similarity': ('Name closely resembles brand', '名稱與品牌高度相似', '名称与品牌高度相似', '名前がブランドと酷似'),
    'code.footprint.claim.same_org_name': ('Same org name (verified)', '相同組織名(已驗證)', '相同组织名(已验证)', '同一組織名 (検証済)'),
    'code.footprint.claim.product_name_mention': ('Product name mention', '提及產品名', '提及产品名', '製品名言及'),
    'code.footprint.claim.news_co_mention': ('News co-mention', '新聞共同提及', '新闻共同提及', 'ニュース共起'),
    'code.footprint.claim.keyword_match': ('Keyword overlap', '關鍵字重疊', '关键字重叠', 'キーワード重複'),
    'code.footprint.claim.fuzzy_brand_similarity': ('Fuzzy brand similarity', '模糊品牌相似度', '模糊品牌相似度', '曖昧ブランド類似'),
    'code.footprint.claim.search_snippet': ('Search snippet', '搜尋摘要', '搜索摘要', '検索スニペット'),
    'code.footprint.claim.different_industry': ('Different industry (penalty)', '不同產業(扣分)', '不同行业(扣分)', '異なる業界 (減点)'),
    'code.footprint.claim.different_country': ('Different country', '不同國家', '不同国家', '異なる国'),
    'code.footprint.claim.whois_ownership_conflict': ('WHOIS ownership conflict', 'WHOIS 所有權衝突', 'WHOIS 所有权冲突', 'WHOIS 所有権の競合'),
    'code.footprint.claim.name_collision_common_word': ('Common-word brand collision', '常用詞品牌撞名', '常用词品牌撞名', '一般語ブランド衝突'),
    'code.unifiedAsset.stat.entities': ('Entities', '資產', '资产', 'アセット'),
    'code.unifiedAsset.stat.subdomains': ('Subdomains', '子網域', '子域名', 'サブドメイン'),
    'code.unifiedAsset.stat.lookalikes': ('Lookalikes', '近似域名', '近似域名', '類似ドメイン'),
    'code.unifiedAsset.stat.actionable': ('Actionable', '可操作', '可操作', '対応可'),
    'code.unifiedAsset.stat.highTierHint': ('high-tier rows', '高等級項目', '高等级项目', '高ティア項目'),
    'code.unifiedAsset.stat.openIssues': ('Open issues', '開啟中問題', '开启中问题', 'オープン項目'),
    'code.unifiedAsset.stat.criticality': ('Criticality', '關鍵度', '关键度', '重要度'),
    'code.unifiedAsset.stat.hasFindings': ('Has findings', '有發現項', '有发现项', '検出項目あり'),
    'code.unifiedAsset.stat.lastScan': ('Last scan', '最近掃描', '最近扫描', '最終スキャン'),
    'code.unifiedAsset.stat.linkedRepos': ('Linked repos', '連結儲存庫', '关联仓库', '関連リポジトリ'),
    'code.unifiedAsset.stat.openAlerts': ('Open alerts', '開啟中警示', '开启中警示', 'オープンアラート'),
    'code.unifiedAsset.stat.eligibleFindings': ('Eligible findings', '可修補的發現項', '可修补的发现项', '対応可な検出項目'),
    'code.unifiedAsset.stat.readyPatches': ('Ready patches', '已備妥的補丁', '已就绪的补丁', '準備済パッチ'),
    'code.unifiedAsset.stat.openPrs': ('Open PRs', '開啟中 PR', '开启中 PR', 'オープン PR'),
    'code.common.yes': ('yes', '是', '是', 'はい'),
    'code.common.no': ('no', '否', '否', 'いいえ'),
    'code.ctemExtras.warroomActions': ('War-room actions', '戰情室操作', '战情室操作', 'ウォールームアクション'),
    'code.ctemExtras.alertHistory': ('Alert history', '警示歷史', '警示历史', 'アラート履歴'),
    'code.ctemExtras.blastGraph': ('Blast-radius graph', '影響範圍圖', '影响范围图', 'ブラスト半径グラフ'),
    'code.ctemExtras.blastRadius': ('Blast radius', '影響範圍', '影响范围', 'ブラスト半径'),
    'code.ctemExtras.aiFix': ('AI-proposed fix', 'AI 建議修補', 'AI 建议修补', 'AI 提案修正'),
    'code.ctemExtras.complianceBinder': ('Compliance evidence binder', '合規證據檔', '合规证据档', 'コンプライアンス証拠バインダー'),
    'code.mit.controlType.waf': ('WAF rule', 'WAF 規則', 'WAF 规则', 'WAF ルール'),
    'code.mit.controlType.edr': ('EDR signature', 'EDR 簽章', 'EDR 签章', 'EDR シグネチャ'),
    'code.mit.controlType.patch': ('Patch baseline', '修補基準', '修补基线', 'パッチベースライン'),
    'code.mit.controlType.segmentation': ('Network segmentation', '網路分段', '网络分段', 'ネットワークセグメント'),
    'code.mit.controlType.scan': ('Scan exclusion / verified', '掃描例外 / 已驗證', '扫描例外 / 已验证', 'スキャン除外 / 検証済'),
    'code.mit.controlType.manual': ('Manual / runbook', '手動 / runbook', '手动 / runbook', '手動 / runbook'),
    'code.mit.evidenceTier.verified.label': ('Auto-verified', '自動驗證', '自动验证', '自動検証済'),
    'code.mit.evidenceTier.verified.hint': ('Automated probe within 24h confirms this control is live.', '24 小時內的自動探測確認控制有效。', '24 小时内的自动探测确认控制有效。', '24時間以内の自動プローブが有効性を確認。'),
    'code.mit.evidenceTier.fading.label': ('Fading', '正在淡化', '正在淡化', 'フェード中'),
    'code.mit.evidenceTier.fading.hint': ('Last probe 1-7d ago. Priority engine applies 75% of the reduction.', '上次探測 1-7 天前。優先級引擎套用 75% 折扣。', '上次探测 1-7 天前。优先级引擎套用 75% 折扣。', '前回プローブから 1-7 日。優先度エンジンは 75% 削減を適用。'),
    'code.mit.evidenceTier.stale.label': ('Stale', '已過期', '已过期', '古い'),
    'code.mit.evidenceTier.stale.hint': ('Last probe 7-30d ago. Priority engine applies 50% of the reduction.', '上次探測 7-30 天前。優先級引擎套用 50% 折扣。', '上次探测 7-30 天前。优先级引擎套用 50% 折扣。', '前回プローブから 7-30 日。優先度エンジンは 50% 削減を適用。'),
    'code.mit.evidenceTier.aspirational.label': ('Aspirational', '僅聲明', '仅声明', '申告のみ'),
    'code.mit.evidenceTier.aspirational.hint': ('No recent automated proof OR last probe failed — priority engine ignores this reduction.', '無近期自動證明或上次探測失敗 — 優先級引擎忽略此折扣。', '无近期自动证明或上次探测失败 — 优先级引擎忽略此折扣。', '最近の自動証明なし or 前回プローブ失敗 — 優先度エンジンはこの削減を無視。'),
    'code.mit.evidenceTier.lastCheck': ('Last check', '上次檢查', '上次检查', '前回チェック'),
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
