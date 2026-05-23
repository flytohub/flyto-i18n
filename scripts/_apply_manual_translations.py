#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    # Sensor map — replace misleading "origin/attacker" labels with
    # explicit "hosting country" + GeoIP disclaimer
    'code.threatIntel.topHosting': (
        'Top hosting country',
        '主要託管國',
        '主要托管国',
        '主要ホスティング国',
    ),
    'code.threatIntel.hostingDistribution': (
        'Malicious-IP hosting country distribution',
        '惡意 IP 的託管國分布',
        '恶意 IP 的托管国分布',
        '悪意 IP のホスティング国分布',
    ),
    'code.threatIntel.geoIpNote': (
        'GeoIP-based: shows where the malicious IPs / C2 / malware URLs are hosted, not who is behind them. Most attackers rent or compromise US-hosted cloud (AWS / GCP / CloudFront), so US dominates regardless of actual threat-actor nationality. For attribution, see Threat Actors.',
        '基於 GeoIP:顯示惡意 IP / C2 / 惡意程式 URL「託管在哪裡」,不是「誰在背後」。多數攻擊者租用或入侵美國雲端(AWS / GCP / CloudFront),所以不管實際威脅組織國籍為何,美國總是最多。歸屬請看「威脅行為者」頁面。',
        '基于 GeoIP:显示恶意 IP / C2 / 恶意程序 URL "托管在哪里",不是 "谁在背后"。多数攻击者租用或入侵美国云端(AWS / GCP / CloudFront),所以不管实际威胁组织国籍为何,美国总是最多。归属请看 "威胁行为者" 页面。',
        'GeoIP ベース: 悪意 IP / C2 / マルウェア URL の「ホスティング場所」を示し、「背後の人物」ではありません。多くの攻撃者は米国ホスト型クラウド(AWS / GCP / CloudFront)を借用または侵害するため、実際の脅威アクター国籍に関係なく米国が常に最多になります。アトリビューションは「脅威アクター」ページを参照。',
    ),
    # Replace the misleading globe + legend labels (keys already exist, overwrite)
    'code.threatIntel.globeTitle': (
        'Malicious-IP hosting globe (GeoIP)',
        '惡意 IP 託管地球 (GeoIP)',
        '恶意 IP 托管地球 (GeoIP)',
        '悪意 IP ホスティンググローブ (GeoIP)',
    ),
    'code.threatIntel.attacker': (
        'Hosting country',
        '託管國',
        '托管国',
        'ホスティング国',
    ),
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
