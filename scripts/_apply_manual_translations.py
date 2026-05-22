#!/usr/bin/env python3
"""Batch translation applier."""
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'
T: dict[str, tuple[str, str, str]] = {}
def add(d): T.update(d)

# ── BATCH 5 — footprint (128) ──
add({
    'code.footprint.action.hideLabels': ('隱藏標籤', '隐藏标签', 'ラベルを隠す'),
    'code.footprint.action.labels': ('標籤', '标签', 'ラベル'),
    'code.footprint.action.pan': ('平移', '平移', 'パン'),
    'code.footprint.action.recenter': ('重置相機', '重置相机', 'カメラリセット'),
    'code.footprint.action.reset': ('重置', '重置', 'リセット'),
    'code.footprint.action.rotate': ('旋轉', '旋转', '回転'),
    'code.footprint.action.showLabels': ('顯示標籤', '显示标签', 'ラベルを表示'),
    'code.footprint.action.zoom': ('縮放', '缩放', 'ズーム'),
    'code.footprint.actionableOnly': ('僅可操作', '仅可操作', '対応可のみ'),
    'code.footprint.autoRun': ('每 24 小時自動執行', '每 24 小时自动执行', '24時間ごとに自動実行'),
    'code.footprint.brief.entities': ('已發現資產', '已发现资产', '検出アセット'),
    'code.footprint.brief.s1.empty': ('AI 摘要完成後會顯示攻擊者視角的敘述。', 'AI 摘要完成后会显示攻击者视角的叙述。', 'AI サマリー完了後、攻撃者視点のナラティブが表示されます。'),
    'code.footprint.brief.s1.title': ('目標檔案', '目标档案', 'ターゲットプロファイル'),
    'code.footprint.brief.s2.empty': ('尚未發現子網域。請先執行「域名與 API」掃描以填入資料。', '尚未发现子域名。请先执行"域名与 API"扫描以填入数据。', 'サブドメイン未検出。先に「ドメイン & API」スキャンを実行してください。'),
    'code.footprint.brief.s2.sub': ('暴露於網際網路的子網域與可達主機。', '暴露于互联网的子域名与可达主机。', 'インターネットに露出したサブドメインと到達可能ホスト。'),
    'code.footprint.brief.s2.title': ('外部攻擊面', '外部攻击面', '外部アタックサーフェス'),
    'code.footprint.brief.s3.sub': ('攻擊者看到您技術堆疊前的東西 — WAF、CDN、框架、廠商。', '攻击者看到您技术栈前的东西 — WAF、CDN、框架、厂商。', '攻撃者があなたの技術スタックの前に見るもの — WAF、CDN、フレームワーク、ベンダー。'),
    'code.footprint.brief.s3.title': ('技術指紋', '技术指纹', 'テクノロジーフィンガープリント'),
    'code.footprint.brief.s4.sub': ('處理電子郵件的網域與外洩文件參考。', '处理电子邮件的域名与泄露文件参考。', 'メール処理ドメインと漏洩文書参照。'),
    'code.footprint.brief.s4.title': ('帳密曝露', '账密暴露', '資格情報露出'),
    'code.footprint.brief.s5.empty': ('尚無紅隊可操作的發現項。', '尚无红队可操作的发现项。', 'レッドチーム対応可な検出項目なし。'),
    'code.footprint.brief.s5.hint': ('再執行時填入「進階 ▸ 候選別名」,或等候 worker 自動循環收集更多來源。', '再执行时填入"高级 ▸ 候选别名",或等候 worker 自动循环收集更多来源。', '「詳細 ▸ 候補エイリアス」を入力して再実行、または worker 自動ループでソース収集を待ってください。'),
    'code.footprint.brief.s5.sub': ('依據我們發現的內容,攻擊者最可能先嘗試的入侵向量。', '依据我们发现的内容,攻击者最可能先尝试的入侵向量。', '我々が発見した内容に基づく、攻撃者が最初に試行する可能性の高いベクトル。'),
    'code.footprint.brief.s5.title': ('可能的初始入侵路徑', '可能的初始入侵路径', '想定される初期アクセス経路'),
    'code.footprint.brief.s6.sub': ('依攻擊情境分組的發現項 — 操作員可動的分桶,而非攻擊配方。', '按攻击情境分组的发现项 — 操作员可动的分桶,而非攻击配方。', '攻撃シナリオでグループ化された検出項目 — 操作員対応可なバケット、エクスプロイトレシピではない。'),
    'code.footprint.brief.s6.title': ('建議紅隊情境', '建议红队情境', '推奨レッドチームシナリオ'),
    'code.footprint.brief.s7.handles': ('已浮現的公開帳號:', '已浮现的公开账号:', '検出された公開ハンドル:'),
    'code.footprint.brief.s7.sub': ('切換到「清單」或「3D」檢視可看完整圖譜。依類型統計:', '切换到"列表"或"3D"视图可看完整图谱。按类型统计:', '「リスト」または「3D」ビューに切替で完全グラフ表示。種別統計:'),
    'code.footprint.brief.s7.title': ('探勘地圖', '探勘地图', 'ディスカバリーマップ'),
    'code.footprint.brief.s8.cta': ('開啟證據包 PDF', '打开证据包 PDF', '証拠パッケージ PDF を開く'),
    'code.footprint.brief.s8.sub': ('產生可列印的偵察簡報 PDF — 目標檔案、攻擊者視角敘述、主要發現項與原因代碼、發現鏈、recon 模式限制。可交付法務、稽核或客戶。', '生成可打印的侦察简报 PDF — 目标档案、攻击者视角叙述、主要发现项与原因代码、发现链、recon 模式限制。可交付法务、审计或客户。', '印刷可能な偵察ブリーフ PDF を生成 — ターゲットプロファイル、攻撃者視点ナラティブ、主要検出項目と理由コード、発見チェーン、recon モード制限。法務、監査、顧客への提出可。'),
    'code.footprint.brief.s8.title': ('匯出證據包', '导出证据包', '証拠パッケージをエクスポート'),
    'code.footprint.brief.types': ('資產類型', '资产类型', 'アセット種別'),
    'code.footprint.delta.added': ('已新增足跡', '已新增足迹', 'フットプリント追加'),
    'code.footprint.delta.more': ('+ {n} 更多', '+ {n} 更多', '+ {n} 件追加'),
    'code.footprint.delta.phase1': ('僅 Phase 1', '仅 Phase 1', 'Phase 1 のみ'),
    'code.footprint.delta.title': ('Phase 2 補上的資產', 'Phase 2 补上的资产', 'Phase 2 で追加されたアセット'),
    'code.footprint.depth': ('深度', '深度', '深度'),
    'code.footprint.feedback.down': ('等級錯誤', '等级错误', 'ティア誤り'),
    'code.footprint.feedback.prompt': ('判定看起來正確嗎?', '判定看起来正确吗?', '判定は正しいですか?'),
    'code.footprint.feedback.thanks': ('感謝 — 分類器權重會在下次彙整時調整為操作員的判斷。', '感谢 — 分类器权重会在下次汇总时调整为操作员的判断。', 'ありがとう — 分類器の重みは次回集約時に操作員の判断に合わせて調整されます。'),
    'code.footprint.feedback.unsure': ('不確定', '不确定', '不明'),
    'code.footprint.feedback.up': ('看起來正確', '看起来正确', '正しい'),
    'code.footprint.field.confidenceCap': ('信心上限', '置信上限', '信頼度上限'),
    'code.footprint.field.depth': ('深度', '深度', '深度'),
    'code.footprint.field.edges': ('連線', '边', 'エッジ'),
    'code.footprint.field.entities': ('資產', '资产', 'アセット'),
    'code.footprint.field.firstSeen': ('首次發現', '首次发现', '初回検出'),
    'code.footprint.field.lastSeen': ('最近發現', '最近发现', '最終検出'),
    'code.footprint.field.promotion': ('晉升', '晋升', '昇格'),
    'code.footprint.field.relationship': ('關係', '关系', '関係'),
    'code.footprint.field.signals': ('信號', '信号', 'シグナル'),
    'code.footprint.field.type': ('類型', '类型', '種別'),
    'code.footprint.legend.chainStrong': ('攻擊鏈 — 強', '攻击链 — 强', '攻撃チェーン — 強'),
    'code.footprint.legend.chainWeak': ('攻擊鏈 — 弱', '攻击链 — 弱', '攻撃チェーン — 弱'),
    'code.footprint.legend.indicator': ('指標(廠商 / 技術)', '指标(厂商 / 技术)', 'インジケータ (ベンダー / 技術)'),
    'code.footprint.panel.attackSurface': ('攻擊面', '攻击面', 'アタックサーフェス'),
    'code.footprint.panel.connectorActivity': ('連接器活動', '连接器活动', 'コネクタアクティビティ'),
    'code.footprint.panel.connectorActivity.fixHint': ('空連接器 — 快速修正:', '空连接器 — 快速修正:', '空のコネクタ — 簡易修正:'),
    'code.footprint.panel.connectorActivity.subtitle': ('最近一次執行哪些來源貢獻了證據。', '最近一次执行哪些来源贡献了证据。', '最新実行でどのソースが証拠を提供したか。'),
    'code.footprint.panel.contradicting': ('矛盾證據', '矛盾证据', '矛盾する証拠'),
    'code.footprint.panel.discoveryChain': ('發現鏈', '发现链', '発見チェーン'),
    'code.footprint.panel.export': ('匯出', '导出', 'エクスポート'),
    'code.footprint.panel.exportPack': ('開啟證據包 — 可列印 HTML,按 Cmd+P 存成 PDF', '打开证据包 — 可打印 HTML,按 Cmd+P 存成 PDF', '証拠パッケージを開く — 印刷可能 HTML、Cmd+P で PDF 保存'),
    'code.footprint.panel.narrative': ('攻擊者視角簡報', '攻击者视角简报', '攻撃者視点ブリーフ'),
    'code.footprint.panel.narrative.empty': ('擴展完成後會顯示敘述。', '扩展完成后会显示叙述。', '展開完了後にナラティブが表示されます。'),
    'code.footprint.panel.narrative.fallback': ('AI 服務不可用 — 改顯示結構化摘要。', 'AI 服务不可用 — 改显示结构化摘要。', 'AI プロバイダー利用不可 — 構造化サマリーを代わりに表示。'),
    'code.footprint.panel.narrative.refresh': ('依最新資料重新產生', '按最新数据重新生成', '最新データから再生成'),
    'code.footprint.panel.nextSteps': ('下一步(取得授權後)', '下一步(取得授权后)', '次のステップ (承認後)'),
    'code.footprint.panel.pathScore': ('路徑分數', '路径分数', 'パススコア'),
    'code.footprint.panel.reconRestrictions': ('Recon 模式「不會」做的事', 'Recon 模式"不会"做的事', 'recon モードが「行わない」こと'),
    'code.footprint.panel.seedHint': ('(種子)', '(种子)', '(シード)'),
    'code.footprint.panel.techFingerprint': ('技術指紋', '技术指纹', 'テクノロジーフィンガープリント'),
    'code.footprint.panel.techFingerprint.subtitle': ('攻擊者看到您堆疊前的東西。', '攻击者看到您堆栈前的东西。', '攻撃者がスタックの前に見るもの。'),
    'code.footprint.panel.topPaths': ('主要攻擊路徑', '主要攻击路径', '主要な攻撃パス'),
    'code.footprint.panel.topPaths.empty': ('尚無紅隊可操作的發現項。', '尚无红队可操作的发现项。', 'レッドチーム対応可な検出項目なし。'),
    'code.footprint.panel.topPaths.nextStep': ('→ 填入「進階 ▸ 候選別名」後重新執行', '→ 填入"高级 ▸ 候选别名"后重新执行', '→ 「詳細 ▸ 候補エイリアス」を入力して再実行'),
    'code.footprint.panel.topPaths.reasonAliases': ('未設定 candidate_aliases — 不同組織名稱下的 GitHub 儲存庫會被遺漏(例如 flyto2 → flytohub)', '未设置 candidate_aliases — 不同组织名称下的 GitHub 仓库会被遗漏(例如 flyto2 → flytohub)', 'candidate_aliases 未設定 — 別の組織名の GitHub リポジトリが見落とされる (例 flyto2 → flytohub)'),
    'code.footprint.panel.topPaths.reasonBreach': ('沒有 HIBP API key — 外洩 email + paste 證據被跳過', '没有 HIBP API key — 泄露 email + paste 证据被跳过', 'HIBP API キーなし — 漏洩 email + paste 証拠スキップ'),
    'code.footprint.panel.topPaths.reasonThin': ('公開足跡稀薄 — 小型目標可能真的沒有可操作項', '公开足迹稀薄 — 小型目标可能真的没有可操作项', '公開フットプリントが薄い — 小規模ターゲットは対応可項目がない可能性'),
    'code.footprint.panel.topPaths.why': ('常見原因:', '常见原因:', '一般的な原因:'),
    'code.footprint.panel.validationSignals': ('驗證信號', '验证信号', '検証シグナル'),
    'code.footprint.panel.weakestHop': ('最弱跳點', '最弱跳点', '最弱ホップ'),
    'code.footprint.panel.whyRelated': ('為何與種子相關?', '为何与种子相关?', 'なぜシードと関連?'),
    'code.footprint.pipeline.run': ('執行管線', '执行管线', 'パイプライン実行'),
    'code.footprint.pipeline.running': ('管線執行中…', '管线执行中…', 'パイプライン実行中…'),
    'code.footprint.pipeline.subtitle': ('Phase 1(外部 CTEM / discovery)→ Phase 2(足跡圖譜)→ Phase 3(滲透測試建議)。一鍵跑完三階段;結果透過共用表流轉。', 'Phase 1(外部 CTEM / discovery)→ Phase 2(足迹图谱)→ Phase 3(渗透测试建议)。一键跑完三阶段;结果通过共享表流转。', 'Phase 1 (外部 CTEM / discovery) → Phase 2 (足跡グラフ) → Phase 3 (ペネトレ提案)。1 クリックで 3 フェーズ実行 — 結果は共有テーブル経由でフロー。'),
    'code.footprint.pipeline.title': ('執行完整管線', '执行完整管线', '完全パイプライン実行'),
    'code.footprint.posture.acting': ('處理中', '处理中', '対応中'),
    'code.footprint.posture.healthy': ('健康', '健康', '健全'),
    'code.footprint.posture.title': ('態勢分布', '态势分布', '態勢分布'),
    'code.footprint.posture.watching': ('觀察中', '观察中', '監視中'),
    'code.footprint.run.advancedHint': ('候選別名(例如 flytohub)、品牌變體、負面關鍵字、產業檔案', '候选别名(例如 flytohub)、品牌变体、负面关键字、行业档案', '候補エイリアス (例 flytohub)、ブランドバリエーション、ネガティブキーワード、業界プロファイル'),
    'code.footprint.run.advancedTitle': ('進階設定', '高级设置', '詳細設定'),
    'code.footprint.run.brandNames': ('品牌名稱', '品牌名称', 'ブランド名'),
    'code.footprint.run.brandNames.help': ('您擁有的已驗證品牌變體。視為強證據,不同於候選別名。', '您拥有的已验证品牌变体。视为强证据,不同于候选别名。', '保有する検証済ブランドバリエーション。候補エイリアスと異なり強い証拠扱い。'),
    'code.footprint.run.candidateAliases': ('候選別名', '候选别名', '候補エイリアス'),
    'code.footprint.run.candidateAliases.help': ('此組織的其他名稱 — GitHub 組織、產品名稱、縮寫。以逗號或換行分隔。', '此组织的其他名称 — GitHub 组织、产品名称、缩写。以逗号或换行分隔。', 'この組織の別名 — GitHub 組織、製品名、略称。カンマまたは改行区切り。'),
    'code.footprint.run.cta': ('執行擴展', '执行扩展', '展開を実行'),
    'code.footprint.run.domain': ('主要網域', '主要域名', 'プライマリドメイン'),
    'code.footprint.run.englishName': ('英文 / 正式名稱(選填)', '英文 / 正式名称(选填)', '英文 / 正式名 (任意)'),
    'code.footprint.run.industry': ('產業(選填)', '行业(选填)', '業界 (任意)'),
    'code.footprint.run.industry.help': ('finance / saas / ecommerce — 選擇相符的評分檔案。', 'finance / saas / ecommerce — 选择相符的评分档案。', 'finance / saas / ecommerce — 対応するスコアリングプロファイルを選択。'),
    'code.footprint.run.negativeKeywords': ('負面關鍵字', '负面关键字', 'ネガティブキーワード'),
    'code.footprint.run.negativeKeywords.help': ('證明某資產「不是」您的字詞 — 例如不相關產業、學校或地區名稱。降低誤報。', '证明某资产"不是"您的字词 — 例如不相关行业、学校或地区名称。降低误报。', '対象アセットが「あなたのものでない」と証明する語句 — 無関係な業界、学校、地区名等。誤検知を削減。'),
    'code.footprint.run.orgName': ('組織名稱', '组织名称', '組織名'),
    'code.footprint.run.recommended': ('建議', '建议', '推奨'),
    'code.footprint.run.running': ('執行中…', '执行中…', '実行中…'),
    'code.footprint.run.section.seed': ('種子', '种子', 'シード'),
    'code.footprint.run.subtitle': ('擴展器從種子向外走過公開 OSINT 來源。當 GitHub 組織名與品牌不同時(例如 "flytohub"),請加入候選別名。', '扩展器从种子向外走过公开 OSINT 来源。当 GitHub 组织名与品牌不同时(例如 "flytohub"),请加入候选别名。', 'エクスパンダーはシードから公開 OSINT ソースを外向きに辿ります。GitHub 組織名がブランドと異なる場合 (例 "flytohub")、候補エイリアスを追加してください。'),
    'code.footprint.run.suggested': ('Phase 1 偵測到的關聯別名 — 點擊加入', 'Phase 1 检测到的关联别名 — 点击加入', 'Phase 1 で検出された関連エイリアス — クリックで追加'),
    'code.footprint.run.title': ('開始 Footprint 擴展', '开始 Footprint 扩展', 'Footprint 展開を開始'),
    'code.footprint.timeline': ('時間軸', '时间轴', 'タイムライン'),
    'code.footprint.timeline.clear': ('顯示全部', '显示全部', 'すべて表示'),
    'code.footprint.tuning.adjust': ('調整', '调整', '調整'),
    'code.footprint.tuning.defaultWeight': ('預設權重', '默认权重', 'デフォルト重み'),
    'code.footprint.tuning.effective': ('生效', '生效', '実効'),
    'code.footprint.tuning.openButton': ('調整此組織的分類器權重', '调整此组织的分类器权重', 'この組織の分類器重みを調整'),
    'code.footprint.tuning.override': ('覆寫', '覆写', 'オーバーライド'),
    'code.footprint.tuning.reason': ('原因(操作員可見的稽核紀錄)', '原因(操作员可见的审计记录)', '理由 (操作員に見える監査ログ)'),
    'code.footprint.tuning.reason.example': ('例如 金融客戶更在意品牌冒用', '例如 金融客户更在意品牌冒用', '例: 金融顧客はブランドなりすましをより重視'),
    'code.footprint.tuning.reset': ('重置為預設', '重置为默认', 'デフォルトにリセット'),
    'code.footprint.tuning.save': ('儲存覆寫', '保存覆写', 'オーバーライドを保存'),
    'code.footprint.tuning.subtitle': ('調整此組織各 claim 的權重。Delta 限制在 [-50, +50]。下次擴展執行時生效。', '调整此组织各 claim 的权重。Delta 限制在 [-50, +50]。下次扩展执行时生效。', 'この組織の claim 別重みを調整。Delta は [-50, +50] にクランプ。次回展開実行時に適用。'),
    'code.footprint.tuning.title': ('分類器規則調整', '分类器规则调整', '分類器ルール調整'),
    'code.footprint.viewMode.brief': ('簡報', '简报', 'ブリーフ'),
    'code.footprint.viewMode.graph': ('3D', '3D', '3D'),
    'code.footprint.viewMode.list': ('清單', '列表', 'リスト'),
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
