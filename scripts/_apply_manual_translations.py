#!/usr/bin/env python3
"""Batch translation applier."""
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'
T: dict[str, tuple[str, str, str]] = {}
def add(d): T.update(d)

# ── BATCH 4 — threatIntel + history + warroom + paths ──

add({
    # threatIntel (63)
    'code.threatIntel.activeOrigins': ('來源國家', '来源国家', '発信国'),
    'code.threatIntel.actorEmpty': ('尚未載入威脅行為者。MITRE ATT&CK 收集器會在下一次 worker tick 執行;剛部署後第一次重新整理可能需要幾分鐘。', '尚未加载威胁行为者。MITRE ATT&CK 收集器会在下一次 worker tick 执行;刚部署后第一次刷新可能需要几分钟。', '脅威アクター未読込。MITRE ATT&CK インジェスターは次の worker tick で実行 — デプロイ直後の初回更新は数分かかります。'),
    'code.threatIntel.actorLibrary': ('威脅行為者圖書館', '威胁行为者图书馆', '脅威アクターライブラリ'),
    'code.threatIntel.actorLibraryLede': ('MITRE ATT&CK 追蹤的 APT 組織、犯罪團體與駭客行動主義者。每週更新。', 'MITRE ATT&CK 追踪的 APT 组织、犯罪团体与黑客行动主义者。每周更新。', 'MITRE ATT&CK 追跡の APT グループ、犯罪集団、ハクティビスト。週次更新。'),
    'code.threatIntel.actorLoadError': ('載入威脅行為者失敗。', '加载威胁行为者失败。', '脅威アクターの読み込みに失敗。'),
    'code.threatIntel.actorSearch': ('依名稱或別名搜尋…', '按名称或别名搜索…', '名前またはエイリアスで検索…'),
    'code.threatIntel.allCountries': ('所有國家', '所有国家', 'すべての国'),
    'code.threatIntel.allGroups': ('所有組織', '所有组织', 'すべてのグループ'),
    'code.threatIntel.allPlatforms': ('所有平台', '所有平台', 'すべてのプラットフォーム'),
    'code.threatIntel.allTypes': ('所有類型', '所有类型', 'すべての種別'),
    'code.threatIntel.attackArc': ('攻擊弧線 → HQ', '攻击弧线 → HQ', '攻撃アーク → HQ'),
    'code.threatIntel.attacker': ('攻擊者起源', '攻击者起源', '攻撃元'),
    'code.threatIntel.attacksByCountry': ('依來源國的攻擊', '按来源国的攻击', '発信国別攻撃'),
    'code.threatIntel.col.country': ('國家', '国家', '国'),
    'code.threatIntel.col.firstSeen': ('首次發現', '首次发现', '初回検出'),
    'code.threatIntel.col.group': ('組織', '组织', 'グループ'),
    'code.threatIntel.col.indicator': ('指標', '指标', 'インジケータ'),
    'code.threatIntel.col.kind': ('類型', '类型', '種別'),
    'code.threatIntel.col.lastSeen': ('最近發現', '最近发现', '最終検出'),
    'code.threatIntel.col.published': ('發布', '发布', '公開'),
    'code.threatIntel.col.sector': ('產業', '行业', '業界'),
    'code.threatIntel.col.source': ('來源', '来源', 'ソース'),
    'code.threatIntel.col.victim': ('受害者', '受害者', '被害者'),
    'code.threatIntel.countries': ('國家', '国家', '国'),
    'code.threatIntel.dragHint': ('拖曳旋轉 · 滾輪縮放', '拖动旋转 · 滚轮缩放', 'ドラッグで回転 · スクロールでズーム'),
    'code.threatIntel.globeTitle': ('即時攻擊起源地球', '即时攻击起源地球', 'リアルタイム攻撃元グローブ'),
    'code.threatIntel.hq': ('總部', '总部', 'HQ'),
    'code.threatIntel.iocLookup': ('IoC 查詢', 'IoC 查询', 'IoC 検索'),
    'code.threatIntel.iocLookupError': ('載入 IoC 失敗。', '加载 IoC 失败。', 'IoC の読み込みに失敗。'),
    'code.threatIntel.iocLookupLede': ('入侵指標 — C2 / URL / IP / 釣魚 / 帳密外洩。', '入侵指标 — C2 / URL / IP / 钓鱼 / 账密外泄。', '侵害指標 — C2 / URL / IP / フィッシング / 資格情報露出。'),
    'code.threatIntel.iocSearch': ('搜尋指標值…', '搜索指标值…', 'インジケータ値を検索…'),
    'code.threatIntel.kind': ('類型', '类型', '種別'),
    'code.threatIntel.malwareEmpty': ('目錄尚未填入。MITRE ATT&CK 收集器在 worker 上每週執行一次。', '目录尚未填入。MITRE ATT&CK 收集器在 worker 上每周执行一次。', 'カタログ未投入。MITRE ATT&CK インジェスターは worker で週次実行。'),
    'code.threatIntel.malwareFamilies': ('惡意程式家族與工具', '恶意程序家族与工具', 'マルウェアファミリーとツール'),
    'code.threatIntel.malwareLede': ('MITRE ATT&CK 軟體目錄 — 惡意程式家族與雙用途工具。每週更新。', 'MITRE ATT&CK 软件目录 — 恶意程序家族与双用途工具。每周更新。', 'MITRE ATT&CK ソフトウェアカタログ — マルウェアファミリーと双用途ツール。週次更新。'),
    'code.threatIntel.malwareLoadError': ('載入惡意程式目錄失敗。', '加载恶意程序目录失败。', 'マルウェアカタログの読み込みに失敗。'),
    'code.threatIntel.malwareSearch': ('依名稱或別名搜尋…', '按名称或别名搜索…', '名前またはエイリアスで検索…'),
    'code.threatIntel.noIoCs': ('沒有符合過濾條件的指標。', '没有符合过滤条件的指标。', 'フィルター条件に一致するインジケータなし。'),
    'code.threatIntel.observations': ('觀測', '观测', '観測'),
    'code.threatIntel.page': ('頁', '页', 'ページ'),
    'code.threatIntel.ransomEmpty': ('尚未載入事件。ransomware.live worker 每小時執行一次。', '尚未加载事件。ransomware.live worker 每小时执行一次。', 'インシデント未読込。ransomware.live worker は毎時実行。'),
    'code.threatIntel.ransomLoadError': ('載入事件失敗。', '加载事件失败。', 'インシデントの読み込みに失敗。'),
    'code.threatIntel.ransomSearch': ('搜尋受害者或組織…', '搜索受害者或组织…', '被害者またはグループを検索…'),
    'code.threatIntel.ransomware': ('勒索軟體事件', '勒索软件事件', 'ランサムウェアインシデント'),
    'code.threatIntel.ransomwareLede': ('來自約 80 個勒索軟體集團外洩網站(LockBit、Black Basta、Akira、8base 等)的受害者公告。透過 ransomware.live 每小時鏡像。', '来自约 80 个勒索软件集团泄露网站(LockBit、Black Basta、Akira、8base 等)的受害者公告。通过 ransomware.live 每小时镜像。', '約 80 のランサムウェア集団リークサイト (LockBit、Black Basta、Akira、8base 等) からの被害者主張。ransomware.live 経由で毎時ミラー。'),
    'code.threatIntel.refreshFailed': ('失敗', '失败', '失敗'),
    'code.threatIntel.refreshNow': ('立即重新整理', '立即刷新', '今すぐ更新'),
    'code.threatIntel.refreshTip': ('強制拉取上游目錄(僅管理員)。繞過排程的 boot-jitter 與週循環。', '强制拉取上游目录(仅管理员)。绕过排程的 boot-jitter 与周循环。', '上流カタログを強制取得 (管理者のみ)。スケジューラの boot-jitter と週次 tick をバイパス。'),
    'code.threatIntel.refreshing': ('重新整理中…', '刷新中…', '更新中…'),
    'code.threatIntel.rows': ('列', '行', '行'),
    'code.threatIntel.scope': ('範圍', '范围', 'スコープ'),
    'code.threatIntel.scopeBoth': ('組織 + 全域', '组织 + 全局', '組織 + グローバル'),
    'code.threatIntel.scopeGlobal': ('全域', '全局', 'グローバル'),
    'code.threatIntel.scopeOrg': ('組織', '组织', '組織'),
    'code.threatIntel.sensorEmpty': ('尚無地理定位的威脅觀測。隨著引擎針對攻擊面發現 IP 並透過威脅情資 enrichment 解析,感應器資料會累積。', '尚无地理定位的威胁观测。随着引擎针对攻击面发现 IP 并通过威胁情资 enrichment 解析,感应器数据会累积。', 'ジオロケーション付き脅威観測なし。エンジンがアタックサーフェスに対して IP を発見し脅威インテリで強化するにつれ、センサーデータが蓄積されます。'),
    'code.threatIntel.sensorLoadError': ('載入感應器地圖失敗。', '加载感应器地图失败。', 'センサーマップの読み込みに失敗。'),
    'code.threatIntel.sensorMap': ('感應器情報', '感应器情报', 'センサーインテリジェンス'),
    'code.threatIntel.sensorMapLede': ('針對本組織觀測到的惡意 IP、C2 指標與惡意程式發布 URL 的來源國家。', '针对本组织观测到的恶意 IP、C2 指标与恶意程序发布 URL 的来源国家。', '本組織に対して観測された悪意 IP、C2 インジケータ、マルウェア配布 URL の発信国。'),
    'code.threatIntel.shown': ('顯示中', '显示中', '表示中'),
    'code.threatIntel.topOrigin': ('主要來源', '主要来源', '主な発信元'),
    'code.threatIntel.totalCount': ('總數', '总数', '合計'),
    'code.threatIntel.totalIndicators': ('總計', '总计', '合計'),
    'code.threatIntel.totalObservations': ('總觀測數', '总观测数', '総観測数'),

    # history (38)
    'code.history.annualReport': ('年度報告(今年)', '年度报告(今年)', '年次レポート (今年)'),
    'code.history.apply': ('套用', '应用', '適用'),
    'code.history.auditTimelineSub': ('外部態勢變化、滲透測試執行、SLA 違反、分數變動 — 稽核員會讀的時序證據鏈。', '外部态势变化、渗透测试执行、SLA 违反、分数变动 — 审计员会读的时序证据链。', '外部態勢変化、ペネトレ実行、SLA 違反、スコア変動 — 監査員が読む時系列証拠。'),
    'code.history.auditTimelineTitle': ('稽核時間軸', '审计时间轴', '監査タイムライン'),
    'code.history.byKind': ('依類型', '按类型', '種別別'),
    'code.history.bySeverity': ('依嚴重度', '按严重度', '重大度別'),
    'code.history.clear': ('清除', '清除', 'クリア'),
    'code.history.codeActivitySub': ('程式碼掃描執行、發現項生命週期變化、程式安全分數隨時間移動。', '代码扫描执行、发现项生命周期变化、代码安全分数随时间移动。', 'コードスキャン実行、検出項目ライフサイクル変化、コードセキュリティスコアの推移。'),
    'code.history.codeActivityTitle': ('程式碼活動', '代码活动', 'コードアクティビティ'),
    'code.history.composition': ('組成', '组成', '構成'),
    'code.history.currentWindowReport': ('當前範圍(自訂)', '当前范围(自定义)', '現在の範囲 (カスタム)'),
    'code.history.customRange': ('自訂範圍', '自定义范围', 'カスタム範囲'),
    'code.history.domainFilter': ('網域…', '域名…', 'ドメイン…'),
    'code.history.empty': ('沒有符合過濾的事件。', '没有符合过滤的事件。', 'フィルターに一致するイベントなし。'),
    'code.history.from': ('從', '从', '開始'),
    'code.history.generateReport': ('產生報告', '生成报告', 'レポート生成'),
    'code.history.generating': ('產生中…', '生成中…', '生成中…'),
    'code.history.kpi.critHigh': ('嚴重 / 高', '严重 / 高', '重大/高'),
    'code.history.kpi.daysActive': ('活躍天數', '活跃天数', 'アクティブ日数'),
    'code.history.kpi.events': ('事件', '事件', 'イベント'),
    'code.history.kpi.scoreChange': ('分數 Δ', '分数 Δ', 'スコア Δ'),
    'code.history.kpi.slaBreaches': ('SLA 違反', 'SLA 违反', 'SLA 違反'),
    'code.history.loading': ('載入歷史中…', '加载历史中…', '履歴読み込み中…'),
    'code.history.monthlyReport': ('月度報告(本月)', '月度报告(本月)', '月次レポート (今月)'),
    'code.history.pdfDownloaded': ('PDF 已下載', 'PDF 已下载', 'PDF をダウンロードしました'),
    'code.history.pdfError': ('PDF 匯出失敗', 'PDF 导出失败', 'PDF エクスポートに失敗'),
    'code.history.period.month': ('月', '月', '月'),
    'code.history.period.quarter': ('季', '季', '四半期'),
    'code.history.period.week': ('週', '周', '週'),
    'code.history.period.year': ('年', '年', '年'),
    'code.history.quarterlyReport': ('季度報告(本季)', '季度报告(本季)', '四半期レポート (今四半期)'),
    'code.history.scoreSparklineEmpty': ('需要至少 2 個分數快照才能畫趨勢線。', '需要至少 2 个分数快照才能画趋势线。', 'トレンドラインには最低 2 件のスコアスナップショットが必要。'),
    'code.history.searchPlaceholder': ('搜尋標題或摘要…', '搜索标题或摘要…', 'タイトルまたはサマリーを検索…'),
    'code.history.sectionScore': ('分數趨勢', '分数趋势', 'スコアトレンド'),
    'code.history.snapshots': ('快照', '快照', 'スナップショット'),
    'code.history.timelineLabel': ('時間軸', '时间轴', 'タイムライン'),
    'code.history.to': ('到', '到', '終了'),
    'code.history.weeklyReport': ('週報(本週)', '周报(本周)', '週次レポート (今週)'),

    # paths (20)
    'code.paths.assetsLabel': ('資產', '资产', 'アセット'),
    'code.paths.detected': ('已偵測', '已检测', '検出'),
    'code.paths.drillHint': ('開啟 CTEM Actions 挑選器,依網域 / 儲存庫搜尋以深入各成員發現項。', '打开 CTEM Actions 挑选器,按域名 / 仓库搜索以深入各成员发现项。', 'CTEM アクションのピッカーを開き、ドメイン / リポジトリで検索して各メンバー項目を深掘り。'),
    'code.paths.emptyDesc': ('優先級引擎尚未執行,或沒有發現項可串成鏈。下次掃描後使用「重新計算」更新。', '优先级引擎尚未执行,或没有发现项可串成链。下次扫描后使用"重新计算"更新。', '優先度エンジンが未実行、または項目が連鎖を形成していません。次のスキャン後「再計算」で更新。'),
    'code.paths.emptyTitle': ('沒有偵測到鏈', '没有检测到链', 'チェーン未検出'),
    'code.paths.findingsLabel': ('發現項', '发现项', '検出項目'),
    'code.paths.lede': ('優先級引擎判定可堆疊為真實攻擊的發現項鏈。每條鏈的優先級高於其最高成員。', '优先级引擎判定可堆叠为真实攻击的发现项链。每条链的优先级高于其最高成员。', '優先度エンジンが実際の攻撃にスタック可能と判断した項目チェーン。各チェーンは最高メンバーより上位。'),
    'code.paths.liveMarkedMitigated': ('攻擊路徑已標記為已緩解', '攻击路径已标记为已缓解', '攻撃パスを緩和済にマーク'),
    'code.paths.markMitigated': ('標記為已緩解', '标记为已缓解', '緩和済にマーク'),
    'code.paths.markMitigatedHint': ('從挑選器隱藏此鏈。若底層發現項仍構成鏈,自動重算會重新發出。', '从挑选器隐藏此链。若底层发现项仍构成链,自动重算会重新发出。', 'ピッカーからこのチェーンを非表示。基底項目が依然チェーンを形成するなら自動再計算で再発行。'),
    'code.paths.marking': ('標記中…', '标记中…', 'マーク中…'),
    'code.paths.priorityHint': ('綜合優先級 — 最高成員 + 集中度加成', '综合优先级 — 最高成员 + 集中度加成', '総合優先度 — 最高メンバー + 集中度ボーナス'),
    'code.paths.recompute': ('重新計算', '重新计算', '再計算'),
    'code.paths.recomputing': ('重新計算中…', '重新计算中…', '再計算中…'),
    'code.paths.title': ('攻擊路徑', '攻击路径', '攻撃パス'),
    'code.paths.toastMarkedMitigated': ('已標記為已緩解', '已标记为已缓解', '緩和済にマーク'),
    'code.paths.toastMitigateFailed': ('緩解失敗', '缓解失败', '緩和に失敗'),
    'code.paths.toastRecomputeFailed': ('重新計算失敗', '重新计算失败', '再計算に失敗'),
    'code.paths.toastRecomputedPrefix': ('已重算 —', '已重算 —', '再計算済 —'),
    'code.paths.toastRecomputedSuffix': ('條路徑已偵測', '条路径已检测', 'パス検出'),

    # warroom (23)
    'code.warroom.connectRepos': ('連接儲存庫', '连接仓库', 'リポジトリを接続'),
    'code.warroom.goRepos': ('前往儲存庫', '前往仓库', 'リポジトリへ'),
    'code.warroom.healthLabel': ('戰情室資料', '战情室数据', 'ウォールームデータ'),
    'code.warroom.liveViewUnavailableHint': ('瀏覽器預覽不可用 — flyto-cloud WebSocket 未設定。劇本仍正常執行;此面板只顯示截圖串流。', '浏览器预览不可用 — flyto-cloud WebSocket 未配置。剧本仍正常执行;此面板只显示截图串流。', 'ブラウザプレビュー利用不可 — flyto-cloud WebSocket 未設定。キャンペーンは通常実行中。このパネルはスクリーンショットストリームのみ。'),
    'code.warroom.pipelineRegenAt': ('產生於', '生成于', '生成日時'),
    'code.warroom.pipelineRegenDialogTitle': ('已重新產生 AI 高階摘要', '已重新生成 AI 高级摘要', 'AI エグゼクティブサマリーを再生成'),
    'code.warroom.pipelineRegenSummary': ('重新產生 AI 摘要', '重新生成 AI 摘要', 'AI サマリーを再生成'),
    'code.warroom.redTeamPreviewNote': ('Runner 已驗證範圍 + 認證並規劃步驟。沒有任何流量送出。', 'Runner 已验证范围 + 认证并规划步骤。没有任何流量送出。', 'Runner がスコープ + 認証を検証し、ステップを計画。トラフィックは送信されていません。'),
    'code.warroom.redTeamPreviewPickNote': ('Dry-run 驗證範圍 + 認證但不送出流量。', 'Dry-run 验证范围 + 认证但不发送流量。', 'Dry-run はスコープ + 認証を検証しトラフィックは送信しません。'),
    'code.warroom.redTeamRunnerTip': ('即時 runner 佇列 — 進行中執行 · 剩餘速率限制 token', '即时 runner 队列 — 进行中执行 · 剩余速率限制 token', 'リアルタイム runner キュー — 実行中 · 残レート制限トークン'),
    'code.warroom.runScan': ('執行掃描', '执行扫描', 'スキャン実行'),
    'code.warroom.secNewOrgDesc': ('安全發現項來自您程式碼的掃描。請先連接儲存庫以啟動 SAST + 相依性 + 機密管線。', '安全发现项来自您代码的扫描。请先连接仓库以启动 SAST + 依赖 + 秘密管线。', 'セキュリティ検出項目はコードのスキャンから生成されます。リポジトリを接続して SAST + 依存関係 + シークレットパイプラインを開始してください。'),
    'code.warroom.secNewOrgTitle': ('尚未連接任何儲存庫', '尚未连接任何仓库', 'リポジトリ未接続'),
    'code.warroom.secPrimaryConnect': ('連接儲存庫', '连接仓库', 'リポジトリを接続'),
    'code.warroom.secStep1': ('連接 GitHub 或 GitLab 儲存庫', '连接 GitHub 或 GitLab 仓库', 'GitHub または GitLab リポジトリを接続'),
    'code.warroom.secStep2': ('等候首次掃描 — 通常 1-3 分鐘', '等候首次扫描 — 通常 1-3 分钟', '初回スキャンを待つ — 通常 1-3 分'),
    'code.warroom.secStep3': ('發現項依可利用性 + 可達性自動排序', '发现项按可利用性 + 可达性自动排序', '検出項目は悪用可能性 + 到達可能性で自動優先順位付け'),
    'code.warroom.stepConnect': ('連接 Git 提供商', '连接 Git 提供商', 'Git プロバイダーを接続'),
    'code.warroom.stepConnectHint': ('GitHub 或 GitLab OAuth', 'GitHub 或 GitLab OAuth', 'GitHub または GitLab OAuth'),
    'code.warroom.stepReview': ('在戰情室檢視發現項', '在战情室查看发现项', 'ウォールームで項目を確認'),
    'code.warroom.stepScan': ('執行首次掃描', '执行首次扫描', '初回スキャンを実行'),
    'code.warroom.stepScanHint': ('平均儲存庫約 2 分鐘', '平均仓库约 2 分钟', '平均リポジトリで約 2 分'),
    'code.warroom.verifyLibraryHint': ('注意:掃描器將此儲存庫歸類為函式庫 / SDK。若它確實是純函式庫,動態探測無法證明任何事(無部署 URL)。若您「有」實際部署 — 請在下一步將 target_url 指向實際部署位置後繼續。', '注意:扫描器将此仓库归类为函数库 / SDK。若它确实是纯函数库,动态探测无法证明任何事(无部署 URL)。若您"有"实际部署 — 请在下一步将 target_url 指向实际部署位置后继续。', '注意: スキャナーはこのリポジトリをライブラリ / SDK と分類しました。純粋なライブラリなら動的検証は無意味 (デプロイ済 URL なし)。実際にデプロイ済なら次のステップで target_url を実デプロイに向けて続行してください。'),
})

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
