#!/usr/bin/env python3
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'

ADDS = {
    # Footprint v3 audit catches
    'code.footprint.runHint': ('Up to {n} rounds. Runs in the background — close this page and the expansion keeps going. Live updates resume when you return.', '最多 {n} 輪。在背景執行 — 關閉此頁面後擴展會繼續。回來時自動接續更新。', '最多 {n} 轮。在后台执行 — 关闭此页面后扩展会继续。回来时自动接续更新。', '最大 {n} ラウンド。バックグラウンドで実行 — このページを閉じても展開は継続。戻ったときに更新が再開されます。'),
    'code.footprint.alreadyRunning': ('Already in progress', '進行中', '进行中', '実行中'),
    'code.footprint.reRun': ('Re-run', '重新執行', '重新执行', '再実行'),
    'code.footprint.expansionFailed': ('Expansion failed', '擴展失敗', '扩展失败', '展開失敗'),
    'code.footprint.expansionRunning': ('Expansion running · Round {n} of {total}', '擴展執行中 · 第 {n} / {total} 輪', '扩展执行中 · 第 {n} / {total} 轮', '展開中 · ラウンド {n} / {total}'),
    'code.footprint.entitiesUnit': ('entities', '個實體', '个实体', '件'),
    'code.footprint.tokensUnit': ('tokens', '個 token', '个 token', 'トークン'),
    'code.footprint.detailHintRow': ('Click any row to see its discovery chain, promotion tier, reason codes, and next steps.', '點選任一列查看探勘鏈、晉升等級、原因代碼與下一步。', '点击任一行查看探勘链、晋升等级、原因代码与下一步。', '任意の行をクリックして発見チェーン、昇格ティア、理由コード、次のステップを表示。'),
    'code.footprint.detailHintNode': ('Click any node in the graph to see its discovery chain, promotion tier, reason codes, and next steps.', '點選圖譜中任一節點查看探勘鏈、晉升等級、原因代碼與下一步。', '点击图谱中任一节点查看探勘链、晋升等级、原因代码与下一步。', 'グラフ内の任意のノードをクリックして発見チェーン、昇格ティア、理由コード、次のステップを表示。'),

    # DomainsView CHECK_CATALOG — 31 entries × (title, desc)
    'code.domains.check.jwt_token_has_weak_secret.title': ('JWT token has weak secret', 'JWT token 密鑰過弱', 'JWT token 密钥过弱', 'JWT トークンの秘密鍵が弱い'),
    'code.domains.check.jwt_token_has_weak_secret.desc': ('The JWT token uses a weak or known compromised secret.', 'JWT token 使用弱或已知洩漏的密鑰。', 'JWT token 使用弱或已知泄露的密钥。', 'JWT トークンが弱いまたは既知の侵害された秘密鍵を使用。'),
    'code.domains.check.server_accepts_invalid_jwt_tokens.title': ('Server accepts invalid JWT tokens', '伺服器接受無效的 JWT token', '服务器接受无效的 JWT token', 'サーバーが無効な JWT トークンを受理'),
    'code.domains.check.server_accepts_invalid_jwt_tokens.desc': ('The server accepts JWT tokens with invalid signatures.', '伺服器接受簽名無效的 JWT token。', '服务器接受签名无效的 JWT token。', 'サーバーが無効な署名の JWT トークンを受理。'),
    'code.domains.check.heartbleed_openssl_vulnerability.title': ('Heartbleed OpenSSL Vulnerability', 'Heartbleed OpenSSL 漏洞', 'Heartbleed OpenSSL 漏洞', 'Heartbleed OpenSSL 脆弱性'),
    'code.domains.check.heartbleed_openssl_vulnerability.desc': ('OpenSSL Heartbeat Extension vulnerability.', 'OpenSSL Heartbeat 擴展漏洞。', 'OpenSSL Heartbeat 扩展漏洞。', 'OpenSSL Heartbeat 拡張の脆弱性。'),
    'code.domains.check.csp_header_not_set.title': ('CSP header not set', '未設定 CSP 標頭', '未设置 CSP 头', 'CSP ヘッダー未設定'),
    'code.domains.check.csp_header_not_set.desc': ('Content Security Policy is not configured.', '未配置內容安全政策。', '未配置内容安全策略。', 'コンテンツセキュリティポリシー未設定。'),
    'code.domains.check.hsts_not_enforced.title': ('HSTS not enforced', '未強制 HSTS', '未强制 HSTS', 'HSTS 未強制'),
    'code.domains.check.hsts_not_enforced.desc': ('HTTP Strict Transport Security is not configured.', '未配置 HTTP Strict Transport Security。', '未配置 HTTP Strict Transport Security。', 'HTTP Strict Transport Security 未設定。'),
    'code.domains.check.directory_browsing_detected.title': ('Directory browsing detected', '偵測到目錄瀏覽', '检测到目录浏览', 'ディレクトリブラウジング検出'),
    'code.domains.check.directory_browsing_detected.desc': ('Directory listings are enabled.', '已啟用目錄列表。', '已启用目录列表。', 'ディレクトリ一覧が有効。'),
    'code.domains.check._env_files_exposed.title': ('.env files exposed', '.env 檔案曝露', '.env 文件暴露', '.env ファイル露出'),
    'code.domains.check._env_files_exposed.desc': ('Environment files expose credentials.', '環境變數檔案曝露憑證。', '环境变量文件暴露凭证。', '環境変数ファイルが認証情報を漏洩。'),
    'code.domains.check.server_accepts_none_algorithm_jwt.title': ("Server accepts 'none' algorithm JWT", "伺服器接受 'none' 演算法的 JWT", "服务器接受 'none' 算法的 JWT", "サーバーが 'none' アルゴリズムの JWT を受理"),
    'code.domains.check.server_accepts_none_algorithm_jwt.desc': ("JWT signed with 'none' algorithm bypasses verification.", "使用 'none' 演算法簽名的 JWT 可繞過驗證。", "使用 'none' 算法签名的 JWT 可绕过验证。", "'none' アルゴリズムで署名された JWT は検証をバイパス。"),
    'code.domains.check.server_accepts_self_signed_jwk.title': ('Server accepts self-signed JWK', '伺服器接受自簽 JWK', '服务器接受自签 JWK', 'サーバーが自己署名 JWK を受理'),
    'code.domains.check.server_accepts_self_signed_jwk.desc': ('Self-signed JWK keys allow impersonation.', '自簽 JWK 金鑰可造成冒用。', '自签 JWK 密钥可造成冒用。', '自己署名 JWK 鍵はなりすましを許可。'),
    'code.domains.check.session_cookie_not_secured.title': ('Session cookie not secured', 'Session cookie 未受保護', 'Session cookie 未受保护', 'セッション Cookie 未保護'),
    'code.domains.check.session_cookie_not_secured.desc': ('Session cookie missing httpOnly/secure.', 'Session cookie 缺少 httpOnly/secure 屬性。', 'Session cookie 缺少 httpOnly/secure 属性。', 'セッション Cookie に httpOnly/secure 属性なし。'),
    'code.domains.check.session_token_in_browser_storage.title': ('Session token in browser storage', 'Session token 存於瀏覽器儲存空間', 'Session token 存于浏览器存储', 'セッショントークンがブラウザストレージに保存'),
    'code.domains.check.session_token_in_browser_storage.desc': ('Session tokens in localStorage are vulnerable.', 'localStorage 內的 session token 易遭竊取。', 'localStorage 内的 session token 易遭窃取。', 'localStorage 内のセッショントークンは脆弱。'),
    'code.domains.check.csp_allows_inline_javascript.title': ('CSP allows inline JavaScript', 'CSP 允許 inline JavaScript', 'CSP 允许 inline JavaScript', 'CSP がインライン JS を許可'),
    'code.domains.check.csp_allows_inline_javascript.desc': ('Inline JS is a common XSS vector.', 'Inline JS 是常見的 XSS 入侵向量。', 'Inline JS 是常见的 XSS 入侵向量。', 'インライン JS は一般的な XSS 攻撃ベクター。'),
    'code.domains.check.ssl_certificate_near_expiration.title': ('SSL Certificate near expiration', 'SSL 憑證即將到期', 'SSL 证书即将到期', 'SSL 証明書の有効期限間近'),
    'code.domains.check.ssl_certificate_near_expiration.desc': ('TLS certificate is about to expire.', 'TLS 憑證即將到期。', 'TLS 证书即将到期。', 'TLS 証明書がまもなく失効。'),
    'code.domains.check.csp_does_not_block_eval.title': ('CSP does not block eval()', 'CSP 未封鎖 eval()', 'CSP 未封锁 eval()', 'CSP が eval() をブロックしない'),
    'code.domains.check.csp_does_not_block_eval.desc': ('eval() enables code injection.', 'eval() 可造成程式碼注入。', 'eval() 可造成代码注入。', 'eval() はコードインジェクションを許可。'),
    'code.domains.check.csp_missing_fallback_directive.title': ('CSP missing fallback directive', 'CSP 缺少 fallback 指令', 'CSP 缺少 fallback 指令', 'CSP に fallback 指示がない'),
    'code.domains.check.csp_missing_fallback_directive.desc': ('Browser treats unrestricted content types as allowed.', '瀏覽器將未限定的內容類型視為允許。', '浏览器将未限定的内容类型视为允许。', 'ブラウザは制限なしのコンテンツ種別を許可扱い。'),
    'code.domains.check.site_accessible_over_http.title': ('Site accessible over HTTP', '網站可透過 HTTP 存取', '网站可通过 HTTP 访问', 'サイトが HTTP でアクセス可'),
    'code.domains.check.site_accessible_over_http.desc': ('HTTP without redirect to HTTPS.', '未強制重新導向到 HTTPS。', '未强制重定向到 HTTPS。', 'HTTPS への強制リダイレクトなし。'),
    'code.domains.check.cookie_sent_unencrypted.title': ('Cookie sent unencrypted', 'Cookie 未加密傳輸', 'Cookie 未加密传输', 'Cookie が暗号化なしで送信'),
    'code.domains.check.cookie_sent_unencrypted.desc': ('Cookie without secure flag.', '缺少 secure flag 的 Cookie。', '缺少 secure flag 的 Cookie。', 'secure フラグなしの Cookie。'),
    'code.domains.check.cookie_missing_httponly.title': ('Cookie missing HttpOnly', 'Cookie 缺少 HttpOnly', 'Cookie 缺少 HttpOnly', 'Cookie に HttpOnly なし'),
    'code.domains.check.cookie_missing_httponly.desc': ('JavaScript can access the cookie.', 'JavaScript 可存取此 Cookie。', 'JavaScript 可访问此 Cookie。', 'JavaScript から Cookie アクセス可。'),
    'code.domains.check.missing_anti_clickjacking_header.title': ('Missing anti-clickjacking header', '缺少防點擊劫持標頭', '缺少防点击劫持头', 'クリックジャッキング防止ヘッダーなし'),
    'code.domains.check.missing_anti_clickjacking_header.desc': ('No X-Frame-Options or CSP frame-ancestors.', '無 X-Frame-Options 或 CSP frame-ancestors。', '无 X-Frame-Options 或 CSP frame-ancestors。', 'X-Frame-Options または CSP frame-ancestors なし。'),
    'code.domains.check.x_content_type_options_missing.title': ('X-Content-Type-Options missing', '缺少 X-Content-Type-Options', '缺少 X-Content-Type-Options', 'X-Content-Type-Options なし'),
    'code.domains.check.x_content_type_options_missing.desc': ('MIME-type confusion possible.', '可能造成 MIME-type 混淆。', '可能造成 MIME-type 混淆。', 'MIME タイプ混乱の可能性。'),
    'code.domains.check.spf_not_configured.title': ('SPF not configured', '未設定 SPF', '未配置 SPF', 'SPF 未設定'),
    'code.domains.check.spf_not_configured.desc': ('Email spoofing possible.', '可能造成電郵假冒。', '可能造成邮件伪冒。', 'メール偽装の可能性。'),
    'code.domains.check.dmarc_not_configured.title': ('DMARC not configured', '未設定 DMARC', '未配置 DMARC', 'DMARC 未設定'),
    'code.domains.check.dmarc_not_configured.desc': ('Phishing via your domain possible.', '可能透過您的網域進行釣魚。', '可能通过您的域名进行钓鱼。', '貴ドメインを使ったフィッシングの可能性。'),
    'code.domains.check.server_leaks_x_powered_by.title': ('Server leaks X-Powered-By', '伺服器洩漏 X-Powered-By', '服务器泄漏 X-Powered-By', 'サーバーが X-Powered-By を漏洩'),
    'code.domains.check.server_leaks_x_powered_by.desc': ('Framework information exposed.', '框架資訊外洩。', '框架信息泄漏。', 'フレームワーク情報の露出。'),
    'code.domains.check.cookie_poisoning_possible.title': ('Cookie poisoning possible', '可能造成 Cookie 注入', '可能造成 Cookie 注入', 'Cookie 汚染の可能性'),
    'code.domains.check.cookie_poisoning_possible.desc': ('URL params can set cookie values.', 'URL 參數可設定 cookie 值。', 'URL 参数可设置 cookie 值。', 'URL パラメータが Cookie 値を設定可能。'),
    'code.domains.check.reverse_tabnabbing_possible.title': ('Reverse tabnabbing possible', '可能造成 Reverse tabnabbing', '可能造成 Reverse tabnabbing', 'リバースタブナビングの可能性'),
    'code.domains.check.reverse_tabnabbing_possible.desc': ('Links without noopener noreferrer.', '連結缺少 noopener noreferrer。', '链接缺少 noopener noreferrer。', 'リンクに noopener noreferrer なし。'),
    'code.domains.check.auth_cookie_accessible_from_subdomains.title': ('Auth cookie accessible from subdomains', '驗證 cookie 可由子網域存取', '认证 cookie 可由子域名访问', '認証 Cookie がサブドメインからアクセス可'),
    'code.domains.check.auth_cookie_accessible_from_subdomains.desc': ('Parent domain cookie scope too broad.', '父網域 cookie scope 範圍過大。', '父域名 cookie scope 范围过大。', '親ドメイン Cookie のスコープが広すぎる。'),
    'code.domains.check.source_code_exposed_via_git.title': ('Source code exposed via .git', '原始碼透過 .git 曝露', '源代码通过 .git 暴露', 'ソースコードが .git 経由で露出'),
    'code.domains.check.source_code_exposed_via_git.desc': ('Git repository files publicly accessible.', 'Git 儲存庫檔案可公開存取。', 'Git 仓库文件可公开访问。', 'Git リポジトリファイルが公開アクセス可。'),
    'code.domains.check.graphql_introspection_enabled.title': ('GraphQL introspection enabled', '已啟用 GraphQL introspection', '已启用 GraphQL introspection', 'GraphQL introspection 有効'),
    'code.domains.check.graphql_introspection_enabled.desc': ('Full API schema exposed.', '完整 API schema 外洩。', '完整 API schema 泄漏。', 'API スキーマ全体が露出。'),
    'code.domains.check.server_leaks_info_via_server_header.title': ('Server leaks info via Server header', '伺服器透過 Server 標頭洩漏資訊', '服务器通过 Server 头泄漏信息', 'サーバーが Server ヘッダー経由で情報を漏洩'),
    'code.domains.check.server_leaks_info_via_server_header.desc': ('Server software identity exposed.', '伺服器軟體版本外洩。', '服务器软件版本泄漏。', 'サーバーソフトウェアの素性が露出。'),
    'code.domains.check.dnssec_not_enabled.title': ('DNSSEC not enabled', '未啟用 DNSSEC', '未启用 DNSSEC', 'DNSSEC 無効'),
    'code.domains.check.dnssec_not_enabled.desc': ('DNS responses can be spoofed.', 'DNS 回應可能被偽造。', 'DNS 响应可能被伪造。', 'DNS 応答が偽造される可能性。'),
    'code.domains.check.subresource_integrity_missing.title': ('Subresource Integrity missing', '缺少 Subresource Integrity', '缺少 Subresource Integrity', 'Subresource Integrity なし'),
    'code.domains.check.subresource_integrity_missing.desc': ('External scripts without integrity checks.', '外部 script 缺少完整性檢查。', '外部 script 缺少完整性检查。', '外部スクリプトに整合性チェックなし。'),
    'code.domains.check.csp_allows_inline_css.title': ('CSP allows inline CSS', 'CSP 允許 inline CSS', 'CSP 允许 inline CSS', 'CSP がインライン CSS を許可'),
    'code.domains.check.csp_allows_inline_css.desc': ('Inline CSS can aid social engineering.', 'Inline CSS 可能助長社交工程攻擊。', 'Inline CSS 可能助长社交工程攻击。', 'インライン CSS はソーシャルエンジニアリングを助長。'),
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
