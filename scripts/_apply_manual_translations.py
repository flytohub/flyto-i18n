#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'
T = {}
def add(d): T.update(d)

# BATCH 10 — footprint hardcoded strings (newly wrapped in tOr)
add({
    # tier filter
    'code.footprint.tierFilter.all': ('全部發現項', '全部发现项', 'すべての検出項目'),
    'code.footprint.tierFilter.redTeamActionable': ('紅隊可操作', '红队可操作', 'レッドチーム対応可'),
    'code.footprint.tierFilter.needsMoreEvidence': ('需要更多證據', '需要更多证据', 'さらに証拠が必要'),
    'code.footprint.tierFilter.informational': ('資訊參考', '资讯参考', '情報'),
    'code.footprint.tierFilter.confirmed': ('— 晉升:已確認', '— 晋升:已确认', '— 昇格: 確認済'),
    'code.footprint.tierFilter.candidate': ('— 晉升:候選', '— 晋升:候选', '— 昇格: 候補'),
    'code.footprint.tierFilter.weak': ('— 晉升:弱', '— 晋升:弱', '— 昇格: 弱'),
    # connector progress
    'code.footprint.connector.websiteCrawl': ('爬取首頁 + robots + sitemap', '爬取首页 + robots + sitemap', 'ホームページ + robots + sitemap をクロール'),
    'code.footprint.connector.whoisRdap': ('拉取註冊紀錄(RDAP)', '拉取注册记录(RDAP)', '登録記録を取得 (RDAP)'),
    'code.footprint.connector.ctLog': ('掃描 CT-log 子網域', '扫描 CT-log 子域名', 'CT-log サブドメインを走査'),
    'code.footprint.connector.lookalike': ('探測 dnstwist 變體', '探测 dnstwist 变体', 'dnstwist の派生をプローブ'),
    'code.footprint.connector.wayback': ('讀取 Wayback Machine 歷史', '读取 Wayback Machine 历史', 'Wayback Machine 履歴を読込'),
    'code.footprint.connector.techStack': ('指紋識別技術堆疊', '指纹识别技术栈', '技術スタックをフィンガープリント'),
    'code.footprint.connector.githubOrg': ('搜尋 GitHub 組織與儲存庫', '搜索 GitHub 组织与仓库', 'GitHub 組織とリポジトリを検索'),
    'code.footprint.connector.secEdgar': ('搜尋 SEC 申報 + App Store + 社群帳號', '搜索 SEC 申报 + App Store + 社交账号', 'SEC ファイリング + App Store + ソーシャルプロファイルを検索'),
    'code.footprint.connector.done': ('完成', '完成', '完了'),
    # scenarios
    'code.footprint.scenario.credential': ('帳號初始入侵', '账号初始入侵', '認証情報による初期アクセス'),
    'code.footprint.scenario.codeExposure': ('公開程式碼曝露', '公开代码暴露', '公開コード露出'),
    'code.footprint.scenario.subdomainTakeover': ('子網域 / 廠商風險', '子域名 / 厂商风险', 'サブドメイン / ベンダーリスク'),
    'code.footprint.scenario.emailPhishing': ('電郵釣魚部署', '邮件钓鱼部署', 'メールフィッシング配備'),
    'code.footprint.scenario.lookalike': ('近似域名監控', '近似域名监控', '類似ドメイン監視'),
    # hop labels
    'code.footprint.hop.seed': ('種子', '种子', 'シード'),
    'code.footprint.hop.direct': ('直接', '直接', '直接'),
    'code.footprint.hop.pivot': ('樞紐', '枢纽', '中継'),
    'code.footprint.hop.extended': ('延伸', '延伸', '拡張'),
    'code.footprint.hop.longTail': ('長尾', '长尾', 'ロングテール'),
    # misc
    'code.footprint.legend.title': ('圖例', '图例', '凡例'),
    'code.footprint.promotion.confirmed': ('已確認', '已确认', '確認済'),
    'code.footprint.promotion.candidate': ('候選', '候选', '候補'),
    'code.footprint.signal.label': ('信號', '信号', 'シグナル'),
})

def apply():
    en_path = ROOT / 'en' / 'code.json'
    en = json.loads(en_path.read_text(encoding='utf-8'))
    en_trans = en['translations']
    en_added = 0
    for key in T:
        if key not in en_trans:
            # English fallback = the string in the code
            slug = key.split('.')[-1]
            en_trans[key] = ''  # placeholder; will set via fb below
            en_added += 1
    # Populate EN with the in-code fallback strings — we know them
    EN_FB = {
        'code.footprint.tierFilter.all': 'All findings',
        'code.footprint.tierFilter.redTeamActionable': 'Red-team actionable',
        'code.footprint.tierFilter.needsMoreEvidence': 'Needs more evidence',
        'code.footprint.tierFilter.informational': 'Informational',
        'code.footprint.tierFilter.confirmed': '— Promotion: confirmed',
        'code.footprint.tierFilter.candidate': '— Promotion: candidate',
        'code.footprint.tierFilter.weak': '— Promotion: weak',
        'code.footprint.connector.websiteCrawl': 'Crawling homepage + robots + sitemap',
        'code.footprint.connector.whoisRdap': 'Pulling registration record (RDAP)',
        'code.footprint.connector.ctLog': 'Walking CT-log subdomains',
        'code.footprint.connector.lookalike': 'Probing dnstwist permutations',
        'code.footprint.connector.wayback': 'Reading Wayback Machine history',
        'code.footprint.connector.techStack': 'Fingerprinting tech stack',
        'code.footprint.connector.githubOrg': 'Searching GitHub orgs and repos',
        'code.footprint.connector.secEdgar': 'Searching SEC filings + App Store + social profiles',
        'code.footprint.connector.done': 'done',
        'code.footprint.scenario.credential': 'Credential Initial Access',
        'code.footprint.scenario.codeExposure': 'Public Code Exposure',
        'code.footprint.scenario.subdomainTakeover': 'Subdomain / Vendor Risk',
        'code.footprint.scenario.emailPhishing': 'Email Phishing Setup',
        'code.footprint.scenario.lookalike': 'Lookalike Domain Watch',
        'code.footprint.hop.seed': 'Seed',
        'code.footprint.hop.direct': 'Direct',
        'code.footprint.hop.pivot': 'Pivot',
        'code.footprint.hop.extended': 'Extended',
        'code.footprint.hop.longTail': 'Long-tail',
        'code.footprint.legend.title': 'Legend',
        'code.footprint.promotion.confirmed': 'Confirmed',
        'code.footprint.promotion.candidate': 'Candidate',
        'code.footprint.signal.label': 'Signal',
    }
    for k, v in EN_FB.items():
        en_trans[k] = v
    en_path.write_text(json.dumps(en, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(f'en: added {en_added}')
    # zh-TW / zh-CN / ja
    for lang_idx, lang in enumerate(('zh-TW', 'zh-CN', 'ja')):
        path = ROOT / lang / 'code.json'
        doc = json.loads(path.read_text(encoding='utf-8'))
        applied = 0
        for key, trio in T.items():
            doc['translations'][key] = trio[lang_idx]
            applied += 1
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'{lang}: set {applied}')
    print(f'total: {len(T)}')

if __name__ == '__main__':
    apply()
