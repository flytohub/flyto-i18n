#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    # Footprint multi-line JSX fixes
    'code.footprint.headerTitle': ('Footprint Graph', '足跡圖譜', '足迹图谱', 'フットプリントグラフ'),
    'code.footprint.headerSubtitle': ('Progressive OSINT graph — every entity the expander reached, scored, and gated.', '漸進式 OSINT 圖譜 — 擴展器走過、計分並把關的所有實體。', '渐进式 OSINT 图谱 — 扩展器走过、计分并把关的所有实体。', '段階的 OSINT グラフ — エクスパンダーが到達・スコアリング・ゲーティングしたすべてのエンティティ。'),
    'code.footprint.noEntitiesAtTier': ('No entities at this tier.', '此等級沒有實體。', '此等级没有实体。', 'このティアにエンティティはありません。'),
    'code.footprint.mappingTitle': ('Mapping your footprint', '正在繪製足跡', '正在绘制足迹', 'フットプリントをマッピング中'),
    'code.footprint.roundOfTotal': ('Round {n} of {total}', '第 {n} / {total} 輪', '第 {n} / {total} 轮', 'ラウンド {n} / {total}'),
    'code.footprint.loadFailed': ('Failed to load footprint graph.', '載入足跡圖譜失敗。', '加载足迹图谱失败。', 'フットプリントグラフの読み込みに失敗。'),
    'code.footprint.tellUsHint': ('Tell us your organisation name and primary domain to start mapping the footprint.', '請填入您的組織名稱與主要網域以開始繪製足跡。', '请填入您的组织名称与主要域名以开始绘制足迹。', '組織名と主要ドメインを入力してフットプリントマッピングを開始してください。'),
    'code.footprint.startExpansion': ('Start expansion', '開始擴展', '开始扩展', '展開を開始'),
    # Error pages
    'code.errors.notFoundDesc': ('The page you requested could not be found.', '找不到您要求的頁面。', '找不到您请求的页面。', '要求されたページが見つかりません。'),
    'code.errors.unauthorizedTitle': ('Unauthorized Access', '未授權存取', '未授权访问', '未認可アクセス'),
    'code.errors.unauthorizedDesc': ('You do not have permission to view this page.', '您沒有檢視此頁面的權限。', '您没有查看此页面的权限。', 'このページを表示する権限がありません。'),
    'code.errors.backToHome': ('Back to Home', '回到首頁', '回到首页', 'ホームに戻る'),
    'code.errors.backToSignIn': ('Back to sign-in', '回到登入頁', '回到登录页', 'サインインに戻る'),
    # Auth
    'code.auth.forgotPassword': ('Forgot password?', '忘記密碼?', '忘记密码?', 'パスワードを忘れた?'),
    'code.auth.signIn': ('Sign in', '登入', '登录', 'サインイン'),
    'code.auth.orContinueWith': ('Or continue with', '或繼續使用', '或继续使用', 'または以下で続行'),
    'code.auth.signedOut': ('You have signed out!', '您已登出!', '您已登出!', 'サインアウトしました!'),
    # App / atoms
    'code.app.loadingSlow': ('Loading is taking longer than expected.', '載入時間比預期長。', '加载时间比预期长。', '読み込みに想定より時間がかかっています。'),
    'code.atoms.proactiveCollection': ('Proactive Collection', '主動收集', '主动收集', 'プロアクティブ収集'),
    'code.atoms.shodanEnrichment': ('Shodan Enrichment', 'Shodan 強化', 'Shodan 强化', 'Shodan エンリッチメント'),
    'code.atoms.verifierHealth': ('Verifier Source Health', '驗證來源健康度', '验证源健康度', '検証ソース健全性'),
    # Dashboard 3D empty states
    'code.dashboard.cityEmpty': ('Connect a repository or add a domain to populate the city', '連接儲存庫或新增網域以填入城市', '连接仓库或新增域名以填入城市', 'リポジトリを接続するかドメインを追加してシティを表示'),
    'code.dashboard.dimensionsEmpty': ('Run a scan to populate scoring dimensions', '執行掃描以填入評分維度', '执行扫描以填入评分维度', 'スキャンを実行してスコアリング次元を表示'),
    # Explore / theme
    'code.explore.signUpFree': ('Sign up free', '免費註冊', '免费注册', '無料登録'),
    'code.layout.fontSize': ('Font Size', '字體大小', '字体大小', '文字サイズ'),
    'code.layout.viewSettings': ('View settings as json/query params', '以 JSON / 查詢參數檢視設定', '以 JSON / 查询参数查看设置', 'JSON / クエリパラメータで設定を表示'),
    'code.layout.themeSettings': ('Theme Settings', '主題設定', '主题设置', 'テーマ設定'),
    'code.layout.themeColorOptions': ('Theme Color Options', '主題顏色選項', '主题颜色选项', 'テーマカラーオプション'),
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
