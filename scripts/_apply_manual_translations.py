#!/usr/bin/env python3
"""Batch translation applier."""
import json, sys, io
from pathlib import Path
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
ROOT = Path(__file__).resolve().parent.parent / 'locales' / 'code'
T: dict[str, tuple[str, str, str]] = {}
def add(d): T.update(d)

# ── BATCH 6 — settings (93) ──
add({
    'code.settings.adminOnly': ('此區塊需要 admin 或 owner 權限。您嘗試的變更可能會被伺服器拒絕。', '此区块需要 admin 或 owner 权限。您尝试的变更可能会被服务器拒绝。', 'このセクションは admin または owner 権限が必要です。試行した変更はサーバーで拒否される可能性があります。'),
    'code.settings.bitbucketDesc': ('連接您的 Bitbucket workspace 以匯入儲存庫。', '连接您的 Bitbucket workspace 以导入仓库。', 'Bitbucket workspace を接続してリポジトリをインポート。'),
    'code.settings.budget.add': ('新增', '新增', '追加'),
    'code.settings.budget.addNew': ('新增政策', '新增策略', 'ポリシー追加'),
    'code.settings.budget.desc': ('為紅隊劇本設定 token 用量上限以控管 AI 花費。', '为红队剧本设置 token 用量上限以控制 AI 花费。', 'レッドチームキャンペーンのトークン使用量上限を設定し AI コストを管理。'),
    'code.settings.budget.title': ('劇本預算政策', '剧本预算策略', 'キャンペーン予算ポリシー'),
    'code.settings.cancel': ('取消', '取消', 'キャンセル'),
    'code.settings.ciGate.blockOn': ('封鎖嚴重度', '封锁严重度', 'ブロック重大度'),
    'code.settings.ciGate.blockOnDesc': ('當發現此嚴重度以上的項目時 CI 檢查失敗。', '当发现此严重度以上的项目时 CI 检查失败。', 'この重大度以上の項目検出時に CI チェック失敗。'),
    'code.settings.ciGate.critical': ('嚴重', '严重', '重大'),
    'code.settings.ciGate.error': ('儲存政策失敗', '保存策略失败', 'ポリシー保存失敗'),
    'code.settings.ciGate.failOnIac': ('IaC 嚴重項目失敗', 'IaC 严重项目失败', 'IaC 重大項目で失敗'),
    'code.settings.ciGate.failOnIacDesc': ('當發現嚴重 IaC 錯誤配置時封鎖 CI。', '当发现严重 IaC 错误配置时封锁 CI。', '重大な IaC 設定ミス検出時に CI ブロック。'),
    'code.settings.ciGate.failOnLicense': ('授權問題失敗', '许可证问题失败', 'ライセンス問題で失敗'),
    'code.settings.ciGate.failOnLicenseDesc': ('當偵測到不合規授權時封鎖 CI。', '当检测到不合规许可证时封锁 CI。', '非準拠ライセンス検出時に CI ブロック。'),
    'code.settings.ciGate.failOnSecret': ('機密失敗', '密钥失败', 'シークレットで失敗'),
    'code.settings.ciGate.failOnSecretDesc': ('當發現曝露的機密或憑證時封鎖 CI。', '当发现暴露的密钥或凭证时封锁 CI。', '露出したシークレットや認証情報検出時に CI ブロック。'),
    'code.settings.ciGate.high': ('高及以上', '高及以上', '高以上'),
    'code.settings.ciGate.medium': ('中及以上', '中及以上', '中以上'),
    'code.settings.ciGate.none': ('無(全部允許)', '无(全部允许)', 'なし (すべて許可)'),
    'code.settings.ciGate.requireScan': ('合併前需先掃描', '合并前需先扫描', 'マージ前にスキャン必須'),
    'code.settings.ciGate.requireScanDesc': ('若 PR 分支未跑過掃描則封鎖合併。', '若 PR 分支未跑过扫描则封锁合并。', 'PR ブランチでスキャン未実行ならマージブロック。'),
    'code.settings.ciGate.save': ('儲存政策', '保存策略', 'ポリシー保存'),
    'code.settings.ciGate.saved': ('政策已儲存', '策略已保存', 'ポリシーを保存しました'),
    'code.settings.ciGate.saving': ('儲存中…', '保存中…', '保存中…'),
    'code.settings.ciGate.title': ('CI/CD 閘門政策', 'CI/CD 闸门策略', 'CI/CD ゲートポリシー'),
    'code.settings.confirmDelete': ('確認刪除', '确认删除', '削除を確認'),
    'code.settings.dangerZone': ('危險區', '危险区', '危険ゾーン'),
    'code.settings.delete': ('刪除', '删除', '削除'),
    'code.settings.deleteOrg': ('刪除組織', '删除组织', '組織を削除'),
    'code.settings.deleteOrgDesc': ('永久刪除此組織與其所有資料。此動作無法復原。', '永久删除此组织与其所有数据。此动作无法撤销。', 'この組織とすべてのデータを永久削除。この操作は取り消せません。'),
    'code.settings.events.allActors': ('所有行為者', '所有行为者', 'すべてのアクター'),
    'code.settings.events.allCategories': ('所有類別', '所有类别', 'すべてのカテゴリ'),
    'code.settings.events.allLevels': ('所有層級', '所有级别', 'すべてのレベル'),
    'code.settings.events.allOutcomes': ('所有結果', '所有结果', 'すべての結果'),
    'code.settings.events.col.category': ('類別', '类别', 'カテゴリ'),
    'code.settings.events.col.event': ('事件', '事件', 'イベント'),
    'code.settings.events.col.level': ('層級', '级别', 'レベル'),
    'code.settings.events.col.message': ('訊息', '消息', 'メッセージ'),
    'code.settings.events.col.time': ('時間', '时间', '時刻'),
    'code.settings.events.empty': ('沒有符合過濾的事件。', '没有符合过滤的事件。', 'フィルターに一致するイベントなし。'),
    'code.settings.events.events': ('事件', '事件', 'イベント'),
    'code.settings.events.refresh': ('重新整理', '刷新', '更新'),
    'code.settings.events.scope.admin': ('平台管理員', '平台管理员', 'プラットフォーム管理者'),
    'code.settings.events.scope.org': ('本組織', '本组织', 'この組織'),
    'code.settings.events.searchMessage': ('搜尋訊息', '搜索消息', 'メッセージを検索'),
    'code.settings.events.statLast24h': ('過去 24h', '过去 24h', '過去 24h'),
    'code.settings.events.subtitle.admin': ('跨「所有」組織的內部診斷日誌。可用 org_id 過濾範圍。預設過去 24 小時。', '跨"所有"组织的内部诊断日志。可用 org_id 过滤范围。默认过去 24 小时。', 'すべての組織にまたがる内部診断ログ。org_id でスコープ。デフォルト過去 24h。'),
    'code.settings.events.subtitle.org': ('本組織的內部診斷日誌。預設過去 24 小時。', '本组织的内部诊断日志。默认过去 24 小时。', 'この組織の内部診断ログ。デフォルト過去 24h。'),
    'code.settings.events.title': ('系統事件', '系统事件', 'システムイベント'),
    'code.settings.members.empty': ('連接 source control 提供商以查看組織成員。', '连接 source control 提供商以查看组织成员。', 'ソースコントロールプロバイダーを接続して組織メンバーを表示。'),
    'code.settings.members.expires': ('到期', '到期', '失効'),
    'code.settings.members.invite': ('邀請', '邀请', '招待'),
    'code.settings.members.inviteTitle': ('邀請成員', '邀请成员', 'メンバーを招待'),
    'code.settings.members.noMembers': ('已連接的提供商沒有成員。', '已连接的提供商没有成员。', '接続済プロバイダーにメンバーがいません。'),
    'code.settings.members.noPending': ('沒有待處理的邀請。', '没有待处理的邀请。', '保留中の招待なし。'),
    'code.settings.members.pending': ('待處理', '待处理', '保留中'),
    'code.settings.members.roleAdmin': ('管理員', '管理员', '管理者'),
    'code.settings.members.roleMember': ('成員', '成员', 'メンバー'),
    'code.settings.members.title': ('組織成員', '组织成员', '組織メンバー'),
    'code.settings.orgInfo': ('組織', '组织', '組織'),
    'code.settings.orgName': ('名稱', '名称', '名前'),
    'code.settings.orgSlug': ('代號', '代号', 'スラッグ'),
    'code.settings.revokeKey': ('撤銷', '撤销', '取り消し'),
    'code.settings.revokeKeyDesc': ('撤銷後此 API key 將立即失效。', '撤销后此 API key 将立即失效。', '取り消し後、この API キーは即座に無効化されます。'),
    'code.settings.revokeKeyTitle': ('撤銷 API key?', '撤销 API key?', 'API キーを取り消し?'),
    'code.settings.save': ('儲存', '保存', '保存'),
    'code.settings.saveFailed': ('儲存失敗', '保存失败', '保存失敗'),
    'code.settings.saved': ('已儲存', '已保存', '保存しました'),
    'code.settings.scanners.runNow': ('立即執行', '立即执行', '今すぐ実行'),
    'code.settings.scanners.subtitle': ('註冊表驅動的背景掃描器,在平台上執行中。可即時切換 / 重新排程(無需重新部署)。', '注册表驱动的后台扫描器,在平台上执行中。可即时切换 / 重新排程(无需重新部署)。', 'レジストリ駆動のバックグラウンドスキャナーがプラットフォームで実行中。トグル/再スケジュールはライブ反映 (再デプロイ不要)。'),
    'code.settings.scanners.title': ('平台掃描器', '平台扫描器', 'プラットフォームスキャナー'),
    'code.settings.schedule.active': ('啟用中', '启用中', 'アクティブ'),
    'code.settings.schedule.autoPausedTip': ('此排程因連續失敗已自動暫停。修正底層問題(token 過期、儲存庫已刪除等)後點「恢復」。', '此排程因连续失败已自动暂停。修正底层问题(token 过期、仓库已删除等)后点"恢复"。', 'このスケジュールは連続失敗で自動一時停止。基底の問題 (トークン期限切れ、リポジトリ削除等) 修正後に「再開」をクリック。'),
    'code.settings.schedule.cadence': ('週期', '周期', '間隔'),
    'code.settings.schedule.cadenceDesc': ('此類掃描自動執行的頻率。', '此类扫描自动执行的频率。', 'この種別のスキャンが自動実行される頻度。'),
    'code.settings.schedule.disableTip': ('完全停用此排程', '完全停用此排程', 'このスケジュールを完全に無効化'),
    'code.settings.schedule.disabled': ('已停用', '已停用', '無効'),
    'code.settings.schedule.enableTip': ('重新啟用此排程', '重新启用此排程', 'このスケジュールを再有効化'),
    'code.settings.schedule.failingTip': ('近期執行失敗。排程器使用指數退避;連續失敗 5 次後自動暫停。', '近期执行失败。排程器使用指数退避;连续失败 5 次后自动暂停。', '最近の実行が失敗。スケジューラは指数バックオフ中。連続 5 回失敗で自動一時停止。'),
    'code.settings.schedule.flaky': ('不穩定', '不稳定', '不安定'),
    'code.settings.schedule.justNow': ('剛剛', '刚刚', 'たった今'),
    'code.settings.schedule.lastRun': ('上次執行', '上次执行', '前回実行'),
    'code.settings.schedule.never': ('從未', '从未', '一度もなし'),
    'code.settings.schedule.nextRun': ('下次執行', '下次执行', '次回実行'),
    'code.settings.schedule.notScheduled': ('未排程', '未排程', 'スケジュールなし'),
    'code.settings.schedule.pause': ('暫停', '暂停', '一時停止'),
    'code.settings.schedule.paused': ('已暫停', '已暂停', '一時停止中'),
    'code.settings.schedule.pausedLabel': ('暫停於:', '暂停于:', '一時停止:'),
    'code.settings.schedule.resume': ('恢復', '恢复', '再開'),
    'code.settings.schedule.runNow': ('立即執行', '立即执行', '今すぐ実行'),
    'code.settings.schedule.runNowTip': ('立即觸發一次掃描。不影響下次排程執行。', '立即触发一次扫描。不影响下次排程执行。', '今すぐ 1 回スキャンを実行。次回スケジュール実行には影響なし。'),
    'code.settings.sourceControl': ('版本控制', '版本控制', 'ソースコントロール'),
})

def apply():
    for lang_idx, lang in enumerate(('zh-TW', 'zh-CN', 'ja')):
        path = ROOT / lang / 'code.json'
        doc = json.loads(path.read_text(encoding='utf-8'))
        applied = 0
        for key, trio in T.items():
            if key not in doc['translations']: continue
            if doc['translations'][key] != trio[lang_idx]:
                doc['translations'][key] = trio[lang_idx]
                applied += 1
        path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'{lang}: applied {applied}')
    print(f'total: {len(T)}')

if __name__ == '__main__':
    apply()
