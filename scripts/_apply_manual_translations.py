#!/usr/bin/env python3
"""Apply manual translations for the 1363 missing keys.

Each call to add() merges a batch into TRANSLATIONS; apply() writes
into locales/code/{zh-TW,zh-CN,ja}/code.json. Idempotent — running
the script twice writes the same values.
"""
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

TRANSLATIONS: dict[str, tuple[str, str, str]] = {}

def add(d):
    TRANSLATIONS.update(d)

# ─── BATCH 1 — common UI primitives, queryError, approval, tier, etc. ───
add({
    'code.common.retry': ('重試', '重试', '再試行'),
    'code.common.cancel': ('取消', '取消', 'キャンセル'),
    'code.common.save': ('儲存', '保存', '保存'),
    'code.common.close': ('關閉', '关闭', '閉じる'),
    'code.common.copy': ('複製', '复制', 'コピー'),
    'code.common.copied': ('已複製', '已复制', 'コピー済'),
    'code.common.loading': ('載入中…', '加载中…', '読み込み中…'),
    'code.common.empty': ('無資料', '无数据', 'データなし'),
    'code.common.error': ('錯誤', '错误', 'エラー'),
    'code.common.noData': ('沒有資料', '没有数据', 'データがありません'),
    'code.common.search': ('搜尋', '搜索', '検索'),
    'code.common.filter': ('過濾', '过滤', 'フィルター'),
    'code.common.refresh': ('重新整理', '刷新', '更新'),
    'code.common.viewAll': ('查看全部', '查看全部', 'すべて表示'),
    'code.queryError.signIn': ('登入', '登录', 'サインイン'),
    'code.queryError.retry': ('重試', '重试', '再試行'),
    'code.queryError.theData': ('此資料', '此数据', 'このデータ'),
    'code.queryError.authTitle': ('登入逾期', '登录过期', 'セッション期限切れ'),
    'code.queryError.authDesc': ('您的登入憑證已失效,請重新登入後繼續。', '您的登录凭证已失效,请重新登录后继续。', 'サインイントークンの有効期限が切れました。再度サインインしてください。'),
    'code.queryError.notFoundTitle': ('找不到', '找不到', '見つかりません'),
    'code.queryError.notFoundDesc': ('', '', ''),
    'code.queryError.serverTitle': ('引擎錯誤', '引擎错误', 'エンジンエラー'),
    'code.queryError.serverDesc': ('Flyto 引擎回傳錯誤。通常重試即可。', 'Flyto 引擎返回错误。通常重试即可。', 'Flyto エンジンがエラーを返しました。再試行で解決します。'),
    'code.queryError.networkTitle': ('網路不可用', '网络不可用', 'ネットワーク利用不可'),
    'code.queryError.networkDesc': ('無法連到 Flyto 引擎。請檢查網路後再試。', '无法连到 Flyto 引擎。请检查网络后再试。', 'Flyto エンジンに接続できません。接続を確認して再試行してください。'),
    'code.queryError.unknownTitle': ('發生問題', '发生问题', '問題が発生しました'),
    'code.queryError.unknownDesc': ('', '', ''),
    'code.approval.title': ('待審批', '待审批', '承認待ち'),
    'code.approval.empty': ('沒有等待中的審批', '没有等待中的审批', '保留中の承認はありません'),
    'code.approval.approve': ('核准', '批准', '承認'),
    'code.approval.reject': ('退回', '驳回', '却下'),
    'code.approval.pending': ('等待中', '等待中', '保留中'),
    'code.approval.approved': ('已核准', '已批准', '承認済'),
    'code.approval.rejected': ('已退回', '已驳回', '却下済'),
    'code.approval.requestedBy': ('申請者', '申请者', '申請者'),
    'code.approval.reason': ('原因', '原因', '理由'),
    'code.approval.comment': ('備註', '备注', 'コメント'),
    'code.approval.commentPlaceholder': ('輸入備註…', '输入备注…', 'コメントを入力…'),
    'code.approval.confirmApprove': ('確認核准', '确认批准', '承認を確認'),
    'code.approval.confirmReject': ('確認退回', '确认驳回', '却下を確認'),
    'code.approval.loadFailed': ('載入審批失敗', '加载审批失败', '承認の読み込みに失敗'),
    'code.fixPlan.title': ('修補計畫', '修补计划', '修正計画'),
    'code.fixPlan.subtitle': ('AI 產生的修補路線圖,按週分組。', 'AI 生成的修补路线图,按周分组。', 'AI 生成の修正ロードマップ、週単位。'),
    'code.fixPlan.empty': ('尚未產生修補計畫', '尚未生成修补计划', '修正計画がまだ生成されていません'),
    'code.studio.title': ('Studio', 'Studio', 'スタジオ'),
    'code.studio.aiRecommendations': ('AI 建議', 'AI 建议', 'AI のおすすめ'),
    'code.studio.empty': ('Studio 暫無內容', 'Studio 暂无内容', 'スタジオに内容はありません'),
    'code.scope.placeholder': ('pii、pci、hipaa…', 'pii、pci、hipaa…', 'pii、pci、hipaa…'),
    'code.tier.loading': ('等級…', '等级…', 'ティア…'),
    'code.tier.discoveryRequiredHint': ('此網域尚無 attack surface 資料,請先在「域名」執行 discovery。', '此域名尚无 attack surface 数据,请先在"域名"执行 discovery。', 'このドメインに attack surface データなし。先にドメインページで discovery を実行してください。'),
    'code.tier.discoveryRequired': ('需先探勘', '需先探勘', '先に探索が必要'),
    'code.tier.critical': ('關鍵', '关键', '重大'),
    'code.tier.high': ('高', '高', '高'),
    'code.tier.medium': ('中', '中', '中'),
    'code.tier.low': ('低', '低', '低'),
    'code.priority.base': ('基礎分', '基础分', 'ベース'),
    'code.priority.tier': ('等級加權', '等级加权', 'ティア'),
    'code.priority.exploit': ('利用評估', '利用评估', 'エクスプロイト'),
    'code.priority.mitigation': ('緩解扣分', '缓解扣分', '緩和'),
    'code.priority.sandbox': ('沙盒驗證', '沙盒验证', 'サンドボックス'),
    'code.priority.ariaLabel': ('優先順序拆解', '优先级拆解', '優先度内訳'),
    'code.sidebar.switchOrg': ('切換組織', '切换组织', '組織を切替'),
    'code.scope.label': ('範圍', '范围', 'スコープ'),
    'code.security.placeholder': ('搜尋…', '搜索…', '検索…'),
    'code.upload.dropHere': ('將檔案拖到此處,或點選上傳', '将文件拖到此处,或点击上传', 'ファイルをドロップまたはクリックでアップロード'),
    'code.verify.placeholder': ('輸入備註…', '输入备注…', 'コメントを入力…'),
    'code.reports.placeholder': ('輸入報告名稱', '输入报告名称', 'レポート名を入力'),
    'code.reports.subtitle': ('產生與下載資安態勢報告。', '生成与下载安全态势报告。', 'セキュリティ態勢レポートを生成・ダウンロード。'),
    'code.repos.placeholder': ('搜尋儲存庫…', '搜索仓库…', 'リポジトリを検索…'),
    'code.repoDetail.placeholder': ('搜尋…', '搜索…', '検索…'),
    'code.repoDetail.notFound': ('找不到此儲存庫', '找不到此仓库', 'リポジトリが見つかりません'),
    'code.repoPicker.search': ('搜尋帳號或組織', '搜索账号或组织', 'アカウント / 組織を検索'),
    'code.repoPicker.empty': ('沒有可用的儲存庫', '没有可用的仓库', '利用可能なリポジトリがありません'),
    'code.onboarding.welcome': ('歡迎使用 Flyto2', '欢迎使用 Flyto2', 'Flyto2 へようこそ'),
    'code.onboarding.start': ('開始', '开始', '開始'),
    'code.onboarding.skip': ('略過', '跳过', 'スキップ'),
    'code.compliance.title': ('合規檢查', '合规检查', 'コンプライアンス'),
    'code.compliance.subtitle': ('將發現項對應到 SOC2 / ISO27001 / PCI / OWASP 等框架。', '将发现项映射到 SOC2 / ISO27001 / PCI / OWASP 等框架。', '検出項目を SOC2 / ISO27001 / PCI / OWASP にマッピング。'),
    'code.compliance.empty': ('暫無合規資料', '暂无合规数据', 'コンプライアンスデータはありません'),
    'code.news.title': ('資安新聞', '安全新闻', 'セキュリティニュース'),
    'code.news.subtitle': ('近期 CVE 與威脅情資新聞。', '近期 CVE 与威胁情资新闻。', '最近の CVE と脅威インテリジェンスニュース。'),
    'code.news.empty': ('沒有新聞項目', '没有新闻项目', 'ニュースはありません'),
    'code.news.source': ('來源', '来源', 'ソース'),
    'code.news.published': ('發布時間', '发布时间', '公開日時'),
    'code.orgTree.title': ('組織架構', '组织架构', '組織図'),
    'code.orgTree.empty': ('尚未建立組織架構', '尚未建立组织架构', '組織図がまだ作成されていません'),
    'code.orgTree.addNode': ('新增節點', '新增节点', 'ノードを追加'),
    'code.orgTree.editNode': ('編輯節點', '编辑节点', 'ノードを編集'),
    'code.orgTree.deleteNode': ('刪除節點', '删除节点', 'ノードを削除'),
    'code.orgTree.search': ('搜尋成員或職稱…', '搜索成员或职称…', 'メンバーや役職を検索…'),
    'code.arch.placeholder': ('搜尋元件、API、套件…', '搜索组件、API、包…', 'コンポーネント、API、パッケージを検索…'),
    'code.arch.empty': ('暫無架構資料', '暂无架构数据', 'アーキテクチャデータはありません'),
    'code.arch.loadFailed': ('載入架構資料失敗', '加载架构数据失败', 'アーキテクチャデータの読み込みに失敗'),
    'code.arch.scanRequired': ('需先執行掃描以建立架構索引', '需先执行扫描以建立架构索引', '先にスキャンを実行する必要があります'),
    'code.assetMap.title': ('資產地圖', '资产地图', 'アセットマップ'),
    'code.assetMap.subtitle': ('每個資產的暴露、影響與相依性可視化。', '每个资产的暴露、影响与依赖可视化。', '各アセットの露出、影響、依存関係を可視化。'),
    'code.assetMap.empty': ('沒有可顯示的資產', '没有可显示的资产', '表示できるアセットがありません'),
    'code.bu.filter.all': ('全部 BU', '全部 BU', 'すべての BU'),
    'code.bu.filter.unassigned': ('未指派', '未分配', '未割当'),
    'code.bu.filter.label': ('業務單位', '业务单元', 'ビジネスユニット'),
    'code.bu.filter.placeholder': ('搜尋 BU…', '搜索 BU…', 'BU を検索…'),
    'code.bu.filter.empty': ('尚未建立 BU', '尚未建立 BU', 'BU がまだ作成されていません'),
    'code.bu.list.title': ('BU 清單', 'BU 列表', 'BU リスト'),
    'code.bu.list.add': ('新增 BU', '新增 BU', 'BU を追加'),
    'code.bu.list.edit': ('編輯 BU', '编辑 BU', 'BU を編集'),
    'code.bu.list.delete': ('刪除 BU', '删除 BU', 'BU を削除'),
    'code.bu.list.confirmDelete': ('確認刪除這個 BU?', '确认删除这个 BU?', 'この BU を削除しますか?'),
    'code.bu.list.namePlaceholder': ('BU 名稱', 'BU 名称', 'BU 名'),
    'code.bu.list.codePlaceholder': ('BU 代號', 'BU 代号', 'BU コード'),
    'code.bu.list.descPlaceholder': ('BU 描述', 'BU 描述', 'BU の説明'),
    'code.bu.list.owner': ('負責人', '负责人', '担当者'),
    'code.bu.list.assets': ('關聯資產', '关联资产', '関連アセット'),
    'code.bu.list.unauthorized': ('沒有管理權限', '没有管理权限', '管理権限がありません'),
    'code.bu.list.unauthorizedHint': ('需要 admin 或 owner 角色才能管理 BU。', '需要 admin 或 owner 角色才能管理 BU。', 'BU の管理には admin または owner ロールが必要です。'),
    'code.bu.list.saveError': ('儲存 BU 失敗', '保存 BU 失败', 'BU の保存に失敗'),
    'code.buassign.success': ('已更新業務單位', '已更新业务单元', 'ビジネスユニットを更新しました'),
    'code.buassign.unassigned': ('未指派 BU', '未分配 BU', 'BU 未割当'),
    'code.buassign.tooltip': ('點選將此資產指派到業務單位', '点击将此资产分配到业务单元', 'クリックしてアセットをビジネスユニットに割り当て'),
    'code.buassign.unassign': ('取消指派 / 全組織', '取消分配 / 全组织', '割当解除 / 組織全体'),
    'code.integrationHealth.title': ('整合健康度', '集成健康度', '統合の健全性'),
    'code.integrationHealth.subtitle': ('連線、API key、最後同步時間。', '连线、API key、最后同步时间。', '接続、API キー、最終同期時刻。'),
    'code.integrationHealth.empty': ('沒有已連線的整合', '没有已连线的集成', '接続済の統合はありません'),
    'code.integrationHealth.connect': ('連線', '连线', '接続'),
    'code.githubAppCallback.title': ('GitHub App 安裝完成', 'GitHub App 安装完成', 'GitHub App インストール完了'),
    'code.githubAppCallback.success': ('已成功安裝,你可以關閉此視窗。', '已成功安装,你可以关闭此窗口。', 'インストールに成功しました。このウィンドウを閉じてください。'),
    'code.githubAppCallback.error': ('安裝失敗,請重試或聯繫管理員。', '安装失败,请重试或联系管理员。', 'インストールに失敗しました。再試行または管理者にお問い合わせください。'),
    'code.githubAppCallback.installFailed': ('安裝失敗', '安装失败', 'インストール失敗'),
    'code.githubAppCallback.installCancelled': ('使用者取消安裝', '用户取消安装', 'ユーザーがインストールをキャンセル'),
    'code.githubAppCallback.installPending': ('GitHub 已批准,正在同步…', 'GitHub 已批准,正在同步…', 'GitHub が承認しました、同期中…'),
    'code.githubAppCallback.gotoApp': ('回到 Flyto', '回到 Flyto', 'Flyto に戻る'),
    'code.githubAppCallback.gotoSettings': ('前往設定', '前往设置', '設定へ'),
    'code.canonical.fingerprintLabel': ('指紋', '指纹', 'フィンガープリント'),
    'code.canonical.merged': ('已合併', '已合并', 'マージ済'),
    'code.canonical.openInGitHub': ('在 GitHub 開啟', '在 GitHub 打开', 'GitHub で開く'),
    'code.canonical.cve': ('CVE 編號', 'CVE 编号', 'CVE 番号'),
    'code.canonical.severity': ('嚴重度', '严重度', '重大度'),
    'code.canonical.fingerprint': ('指紋', '指纹', 'フィンガープリント'),
    'code.canonical.firstSeen': ('首次發現', '首次发现', '初回検出'),
    'code.canonical.lastSeen': ('最近更新', '最近更新', '最終更新'),
    'code.canonical.affectedAssets': ('影響資產', '影响资产', '影響アセット'),
    'code.canonical.duplicates': ('重複', '重复', '重複'),
    'code.canonical.empty': ('沒有可合併的項目', '没有可合并的项目', 'マージ対象がありません'),
})

def apply():
    for lang_idx, lang in enumerate(('zh-TW', 'zh-CN', 'ja')):
        path = ROOT / lang / 'code.json'
        doc = json.loads(path.read_text(encoding='utf-8'))
        applied = 0
        for key, trio in TRANSLATIONS.items():
            if key not in doc['translations']:
                continue
            new_val = trio[lang_idx]
            if doc['translations'][key] != new_val:
                doc['translations'][key] = new_val
                applied += 1
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'{lang}: applied {applied}')
    print(f'total in dict: {len(TRANSLATIONS)}')

if __name__ == '__main__':
    apply()
