#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    # AttackPathsView path types + edge kinds
    'code.paths.type.crown_jewel_concentration.label': ('Crown-jewel concentration', '皇冠級資產集中', '皇冠级资产集中', '最重要資産の集中'),
    'code.paths.type.crown_jewel_concentration.hint': ('Multiple findings stacked on one high-value asset — any one is the foothold.', '單一高價值資產上堆積多個發現項 — 任一都是入侵點。', '单一高价值资产上堆积多个发现项 — 任一都是入侵点。', '1 つの高価値アセットに複数の項目が積層 — どれもが足がかり。'),
    'code.paths.type.edge_to_internal.label': ('Edge-to-internal', '邊界到內部', '边界到内部', 'エッジから内部'),
    'code.paths.type.edge_to_internal.hint': ('External finding + code finding on the same publishing repo — classic public→source chain.', '外部發現項 + 同一儲存庫的程式碼發現項 — 經典的公開→原始碼鏈。', '外部发现项 + 同一仓库的代码发现项 — 经典的公开→源码链。', '外部検出項目 + 同一公開リポジトリのコード検出項目 — 公開→ソースの典型チェーン。'),
    'code.paths.type.cred_to_privesc.label': ('Credential-to-privesc', '帳密到提權', '账密到提权', '認証情報から権限昇格'),
    'code.paths.type.cred_to_privesc.hint': ('Exposed credential plus a code-execution / SQLi finding on the same asset — broken auth instantly turns into RCE.', '同一資產上有曝露的帳密加上 RCE/SQLi 發現項 — 失效認證立即升級為 RCE。', '同一资产上有暴露的账密加上 RCE/SQLi 发现项 — 失效认证立即升级为 RCE。', '同一アセットで露出した認証情報 + コード実行 / SQLi 検出 — 認証破綻が即 RCE。'),
    'code.paths.type.graph_chain.label': ('Graph-detected chain', '圖譜偵測的鏈', '图谱检测的链', 'グラフ検出チェーン'),
    'code.paths.type.graph_chain.hint': ('Bounded BFS over the asset+finding graph. Probability = product of per-edge weights.', '在資產+發現項圖上做有界 BFS。機率 = 每條邊權重的乘積。', '在资产+发现项图上做有界 BFS。概率 = 每条边权重的乘积。', 'アセット+検出グラフ上の有界 BFS。確率 = エッジごとの重みの積。'),
    'code.paths.metaDefaultHint': ('Detected chain.', '偵測到的鏈。', '检测到的链。', '検出されたチェーン。'),
    'code.paths.edgeKind.hosted_on': ('exploitable on asset', '資產上可利用', '资产上可利用', 'アセット上で悪用可'),
    'code.paths.edgeKind.anchored_on': ('asset → finding', '資產 → 發現項', '资产 → 发现项', 'アセット → 検出'),
    'code.paths.edgeKind.deploys_to': ('deploys to', '部署到', '部署到', 'デプロイ先'),
    'code.paths.edgeKind.same_root': ('sibling subdomain', '同根子網域', '同根子域名', '兄弟サブドメイン'),
    # ActionItemCard priority/difficulty
    'code.pulse.action.priority.urgent': ('Urgent', '緊急', '紧急', '緊急'),
    'code.pulse.action.priority.important': ('Important', '重要', '重要', '重要'),
    'code.pulse.action.priority.suggested': ('Suggested', '建議', '建议', '推奨'),
    'code.pulse.action.difficulty.quick-win': ('Quick Win', '快速見效', '快速见效', '即効'),
    'code.pulse.action.difficulty.medium': ('Medium', '中等', '中等', '中'),
    'code.pulse.action.difficulty.project': ('Project', '專案級', '项目级', 'プロジェクト'),
    # BrandProtectionView takedown states
    'code.exposure.brand.takedown.detected': ('Detected', '已偵測', '已检测', '検出'),
    'code.exposure.brand.takedown.evidence_collected': ('Evidence collected', '已收集證據', '已收集证据', '証拠収集済'),
    'code.exposure.brand.takedown.submitted': ('Submitted', '已提交', '已提交', '提出済'),
    'code.exposure.brand.takedown.acknowledged': ('Acknowledged', '已接受', '已接受', '受理済'),
    'code.exposure.brand.takedown.resolved': ('Resolved', '已解決', '已解决', '解決済'),
    'code.exposure.brand.takedown.rejected': ('Rejected', '已拒絕', '已拒绝', '却下'),
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
