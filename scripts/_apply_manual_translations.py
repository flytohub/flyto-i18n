#!/usr/bin/env python3
"""Batch translation applier."""
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'
T: dict[str, tuple[str, str, str]] = {}
def add(d): T.update(d)

# ── BATCH 3 — footprint + external + exposure + history + warroom + paths/attackpath + threatIntel ──

add({
    # ── code.attackpath ── (24 keys, namespace is actually 'code.attackpath')
    'code.code.attackpath.collapse': ('收起細節', '收起细节', '詳細を隠す'),
    'code.code.attackpath.confidence.label': ('信心度', '置信度', '信頼度'),
    'code.code.attackpath.confidence.tooltip': ('假設成立的可能性。', '假设成立的可能性。', '仮説の妥当性。'),
    'code.code.attackpath.disclaimer': ('僅 recon 模式 — 不登入、不送 payload、不暴力破解、不超出快取 recon 資料的外部 API 呼叫。所有候選都是需經授權才能交付紅隊驗證的假設。', '仅 recon 模式 — 不登录、不发送 payload、不暴力破解、不超出缓存 recon 数据的外部 API 调用。所有候选都是需经授权才能交付红队验证的假设。', 'recon モードのみ — ログイン、ペイロード、ブルートフォース、キャッシュ済 recon データ以外の外部 API 呼び出しは一切なし。すべての候補は承認後にレッドチーム検証する仮説です。'),
    'code.code.attackpath.empty.low': ('沒有攻擊路徑假設。請執行 discovery 掃描或連接儲存庫以餵入信號收集器。', '没有攻击路径假设。请执行 discovery 扫描或连接仓库以喂入信号收集器。', '攻撃パス仮説なし。discovery スキャンを実行するかリポジトリを接続してシグナルコレクタにフィードしてください。'),
    'code.code.attackpath.empty.medium': ('沒有中信心度以上的候選。切到「全部」可看到值得人工檢視的低信心候選。', '没有中置信度以上的候选。切到"全部"可看到值得人工检视的低置信候选。', '中以上の信頼度候補なし。「すべて」に切替えて、手動レビュー対象の低信頼候補も表示。'),
    'code.code.attackpath.empty.title': ('沒有符合當前過濾的候選', '没有符合当前过滤的候选', '現在のフィルターに一致する候補なし'),
    'code.code.attackpath.expand': ('顯示證據、紅隊驗證與限制', '显示证据、红队验证与限制', '証拠、レッドチーム検証、制限を表示'),
    'code.code.attackpath.filter.confidence.high': ('僅高信心', '仅高置信', '高のみ'),
    'code.code.attackpath.filter.confidence.low': ('全部', '全部', 'すべて'),
    'code.code.attackpath.filter.confidence.medium': ('中以上', '中以上', '中以上'),
    'code.code.attackpath.readiness.label': ('就緒度', '就绪度', '実施可能性'),
    'code.code.attackpath.readiness.tooltip': ('紅隊現在是否可合法且安全地測試。', '红队现在是否可合法且安全地测试。', 'レッドチームが今、合法かつ安全にテスト可能か。'),
    'code.code.attackpath.section.evidence': ('支持證據', '支持证据', '裏付け証拠'),
    'code.code.attackpath.section.red_team': ('紅隊驗證', '红队验证', 'レッドチーム検証'),
    'code.code.attackpath.section.restrictions': ('Recon 模式限制', 'Recon 模式限制', 'recon モード制限'),
    'code.code.attackpath.section.risk_logic': ('風險邏輯', '风险逻辑', 'リスクロジック'),
    'code.code.attackpath.sort.confidence': ('依信心度', '按置信度', '信頼度順'),
    'code.code.attackpath.sort.readiness': ('依就緒度', '按就绪度', '実施可能性順'),
    'code.code.attackpath.sort.why_now': ('依新近性', '按新近性', '新しさ順'),
    'code.code.attackpath.subtitle': ('攻擊者會從哪裡開始,以及為什麼 — 從現有 recon 信號彙聚為值得紅隊驗證的初始存取假設。', '攻击者会从哪里开始,以及为什么 — 从现有 recon 信号汇聚为值得红队验证的初始访问假设。', '攻撃者がどこから始めるか、その理由 — 既存の recon シグナルから収束させた、レッドチーム検証に値する初期アクセス仮説。'),
    'code.code.attackpath.summary.shown': ('顯示中', '显示中', '表示中'),
    'code.code.attackpath.title': ('攻擊路徑', '攻击路径', '攻撃パス'),
    'code.code.attackpath.whynow.today': ('今天', '今天', '今日'),

    # ── exposure ── (37 keys)
    'code.exposure.activity.all': ('全部', '全部', 'すべて'),
    'code.exposure.activity.empty': ('沒有近期活動', '没有近期活动', '最近のアクティビティなし'),
    'code.exposure.activity.emptyHint': ('掃描器執行時,監控與威脅情資事件會出現在此。', '扫描器执行时,监控与威胁情资事件会出现在此。', 'スキャナー実行時、監視と脅威インテリイベントがここに表示されます。'),
    'code.exposure.activity.noMatchingSeverity': ('此嚴重度沒有事件。', '此严重度没有事件。', 'この重大度のイベントなし。'),
    'code.exposure.brand.caseBrandAbuse': ('品牌濫用', '品牌滥用', 'ブランド悪用'),
    'code.exposure.brand.caseFakeSocial': ('假冒社群帳號', '假冒社交账号', '偽ソーシャルアカウント'),
    'code.exposure.brand.caseImpersonation': ('偽冒網站', '冒充网站', 'なりすましサイト'),
    'code.exposure.brand.casePhishing': ('釣魚頁面', '钓鱼页面', 'フィッシングページ'),
    'code.exposure.brand.caseType': ('案件類型', '案件类型', 'ケース種別'),
    'code.exposure.brand.copy': ('複製', '复制', 'コピー'),
    'code.exposure.brand.detectionSection': ('偵測', '检测', '検出'),
    'code.exposure.brand.downloadEvidence': ('下載證據包', '下载证据包', '証拠パッケージをダウンロード'),
    'code.exposure.brand.downloadLetter': ('下載 .md', '下载 .md', '.md をダウンロード'),
    'code.exposure.brand.expiresAt': ('到期', '到期', '失効'),
    'code.exposure.brand.finalURL': ('最終 URL', '最终 URL', '最終 URL'),
    'code.exposure.brand.generateLetter': ('產生下架信草稿', '生成下架信草稿', 'テイクダウンレターを生成'),
    'code.exposure.brand.generic': ('通用', '通用', '汎用'),
    'code.exposure.brand.letterDisclaimer': ('此為由公開證據彙整的「草稿」。請逐項檢視所有聲明,附上您的品牌/商標權證明,並自行向相應的平台/註冊商/託管商提交。Flyto 不會代您送出檢舉。', '此为由公开证据汇总的"草稿"。请逐项检视所有声明,附上您的品牌/商标权证明,并自行向相应的平台/注册商/托管商提交。Flyto 不会代您送出检举。', 'これは公開証拠から作成された「草案」です。各主張を見直し、ブランド/商標権の証明を添付し、対象プラットフォーム/レジストラ/ホスティング業者へ自身で提出してください。Flyto は代理申請しません。'),
    'code.exposure.brand.letterTitle': ('下架信草稿', '下架信草稿', 'テイクダウンレター草案'),
    'code.exposure.brand.lookalikes': ('近似域名', '近似域名', '類似ドメイン'),
    'code.exposure.brand.nameservers': ('名稱伺服器', '名称服务器', 'ネームサーバー'),
    'code.exposure.brand.networkSection': ('網路', '网络', 'ネットワーク'),
    'code.exposure.brand.openSite': ('在新分頁開啟', '在新标签页打开', '新しいタブで開く'),
    'code.exposure.brand.providersSection': ('服務提供商', '服务提供商', 'サービスプロバイダー'),
    'code.exposure.brand.registeredAt': ('註冊時間', '注册时间', '登録日'),
    'code.exposure.brand.registrar': ('註冊商', '注册商', 'レジストラ'),
    'code.exposure.brand.reportAbuse': ('檢舉濫用', '举报滥用', '不正報告'),
    'code.exposure.brand.saveState': ('更新', '更新', '更新'),
    'code.exposure.brand.saved': ('已儲存', '已保存', '保存済'),
    'code.exposure.brand.savingState': ('儲存中…', '保存中…', '保存中…'),
    'code.exposure.brand.shotAlt': ('網站預覽', '网站预览', 'サイトプレビュー'),
    'code.exposure.brand.shotPending': ('預覽產生中', '预览生成中', 'プレビュー保留中'),
    'code.exposure.brand.shotUnavailable': ('預覽不可用', '预览不可用', 'プレビュー利用不可'),
    'code.exposure.brand.takedownStatus': ('下架狀態', '下架状态', 'テイクダウン状態'),
    'code.exposure.brand.targetProvider': ('送往', '发往', '送信先'),
    'code.exposure.brand.trackingPlaceholder': ('追蹤 / 案件 ID', '追踪 / 案件 ID', '追跡 / ケース ID'),
    'code.exposure.brand.whoisSection': ('註冊資訊', '注册信息', '登録情報'),

    # ── external ── (49 keys)
    'code.external.breachIn24h': ('24 小時內', '24 小时内', '24時間以内'),
    'code.external.breachIn72h': ('72 小時內', '72 小时内', '72時間以内'),
    'code.external.breachIn7d': ('7 天內', '7 天内', '7日以内'),
    'code.external.causality': ('因果關係', '因果关系', '因果'),
    'code.external.detailAssets': ('已發現資產', '已发现资产', '検出アセット'),
    'code.external.detailEmptyDesc': ('中間列點任一個網域,這裡會顯示分數、資產數、未修補問題與下一步操作。', '中间列点任一个域名,这里会显示分数、资产数、未修补问题与下一步操作。', '中央のリストでドメインをクリック — スコア、アセット数、未対応項目、次のアクションが表示されます。'),
    'code.external.detailEmptyTitle': ('點選一個網域以查看細節', '点击一个域名以查看细节', 'ドメインをクリックして詳細を表示'),
    'code.external.detailHeader': ('細節', '细节', '詳細'),
    'code.external.detailIssues': ('開啟中問題', '开启中问题', 'オープン項目'),
    'code.external.detailScore': ('分數', '分数', 'スコア'),
    'code.external.detailViewFindings': ('查看此網域的發現項 →', '查看此域名的发现项 →', 'このドメインの検出項目を表示 →'),
    'code.external.errDimActivity': ('活動 feed', '活动 feed', 'アクティビティフィード'),
    'code.external.errDimAssets': ('攻擊面', '攻击面', 'アタックサーフェス'),
    'code.external.errDimCtem': ('CTEM 優先項目', 'CTEM 优先项目', 'CTEM 優先項目'),
    'code.external.errDimPaths': ('攻擊路徑', '攻击路径', '攻撃パス'),
    'code.external.errDimPosture': ('態勢摘要', '态势摘要', '態勢サマリー'),
    'code.external.errDimRuns': ('探勘執行', '探勘执行', 'ディスカバリー実行'),
    'code.external.errDimSnapshots': ('分數趨勢', '分数趋势', 'スコアトレンド'),
    'code.external.errDimSourceHealth': ('驗證來源健康度', '验证来源健康度', '検証ソース健全性'),
    'code.external.generating': ('產生中…', '生成中…', '生成中…'),
    'code.external.outOf100': ('/ 100', '/ 100', '/ 100'),
    'code.external.partialDataDesc': ('以下維度顯示陳舊或空白資料:', '以下维度显示陈旧或空白数据:', '以下の次元が古いまたは空のデータを表示しています:'),
    'code.external.partialDataHint': ('其餘頁面內容仍正確。重試會只更新失敗的維度。', '其余页面内容仍正确。重试会只更新失败的维度。', 'ページの他の部分は正確です。再試行で失敗した次元のみ更新します。'),
    'code.external.partialDataTitle': ('部分態勢資料無法載入', '部分态势数据无法加载', '一部の態勢データを読み込めませんでした'),
    'code.external.pdfDownloaded': ('PDF 已下載', 'PDF 已下载', 'PDF をダウンロードしました'),
    'code.external.pdfError': ('PDF 匯出失敗', 'PDF 导出失败', 'PDF エクスポートに失敗'),
    'code.external.postureTrend90': ('90 日態勢快照', '90 日态势快照', '90日態勢スナップショット'),
    'code.external.postureTrendHint': ('分數 • 發現項 • 資產 — 滑鼠移到任一天可檢視', '分数 • 发现项 • 资产 — 鼠标移到任一天可检视', 'スコア • 検出項目 • アセット — 任意の日にホバーで確認'),
    'code.external.quickAuthVerified': ('已驗證帳號的發現項', '已验证账号的发现项', '認証済検出項目'),
    'code.external.quickBrand': ('品牌防護', '品牌防护', 'ブランド保護'),
    'code.external.quickCrownJewel': ('皇冠級發現項', '皇冠级发现项', '最重要資産項目'),
    'code.external.quickKev': ('KEV 已曝露', 'KEV 已暴露', 'KEV 露出'),
    'code.external.quickMitigations': ('緩解措施', '缓解措施', '緩和策'),
    'code.external.quickPaths': ('攻擊路徑', '攻击路径', '攻撃パス'),
    'code.external.quickPhishing': ('釣魚 URL', '钓鱼 URL', 'フィッシング URL'),
    'code.external.quickSaaSPosture': ('SaaS 態勢問題', 'SaaS 态势问题', 'SaaS 態勢の問題'),
    'code.external.quickStealerLogs': ('Stealer log 命中', 'Stealer log 命中', 'Stealer ログヒット'),
    'code.external.quickSuspCerts': ('可疑憑證', '可疑证书', '疑わしい証明書'),
    'code.external.quickThreatActor': ('有威脅行為者', '有威胁行为者', '脅威アクターあり'),
    'code.external.redactDomains': ('遮蔽網域', '遮蔽域名', 'ドメインを伏字'),
    'code.external.redactHint': ('將公開後綴主機名替換為 ***.tld — 對外分享前可使用。這不是安全邊界,送出前請再核對。', '将公开后缀主机名替换为 ***.tld — 对外分享前可使用。这不是安全边界,送出前请再核对。', '公開サフィックス付きホスト名を ***.tld に置換 — 外部共有時に有用。セキュリティ境界ではないため送信前に確認してください。'),
    'code.external.reportSections': ('報告章節', '报告章节', 'レポートセクション'),
    'code.external.scoreTrend': ('分數趨勢', '分数趋势', 'スコアトレンド'),
    'code.external.tabActivity': ('活動', '活动', 'アクティビティ'),
    'code.external.tabDarkWeb': ('暗網', '暗网', 'ダークウェブ'),
    'code.external.tabOverview': ('總覽', '总览', '概要'),
    'code.external.tabSupply': ('供應鏈', '供应链', 'サプライチェーン'),
    'code.external.upcomingBreaches': ('即將違反 SLA', '即将违反 SLA', 'SLA 違反予測'),
    'code.external.upcomingHint': ('依 first_seen + sla 計算 — 在違反前先處理', '依 first_seen + sla 计算 — 在违反前先处理', 'first_seen + sla から計算 — 違反前に対応'),
})

# Save what we have (footprint/threatIntel/history/warroom/paths next batch)
def apply():
    for lang_idx, lang in enumerate(('zh-TW', 'zh-CN', 'ja')):
        path = ROOT / lang / 'code.json'
        doc = json.loads(path.read_text(encoding='utf-8'))
        applied = 0
        for key, trio in T.items():
            if key not in doc['translations']:
                continue
            new_val = trio[lang_idx]
            if doc['translations'][key] != new_val:
                doc['translations'][key] = new_val
                applied += 1
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'{lang}: applied {applied}')
    print(f'total in dict: {len(T)}')

if __name__ == '__main__':
    apply()
