#!/usr/bin/env python3
"""Fill remaining zh-TW translations that still equal English."""
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent

ZH = {
    # admin.telemetry
    "admin.telemetry.health.currentStatus": "目前狀態",
    "admin.telemetry.health.failures": "失敗次數",
    "admin.telemetry.health.recentChecks": "最近檢查",
    "admin.telemetry.health.totalChecks": "總檢查數",
    "admin.telemetry.health.uptime": "正常運行時間",
    "admin.telemetry.insights.anthropicApiKey": "Anthropic API 金鑰",
    "admin.telemetry.insights.discordWebhookUrl": "Discord Webhook 網址",
    "admin.telemetry.tabs.health": "健康狀態",
    "admin.factory.url": "Zapier 網址",

    # aiAgent
    "aiAgent.apiKeyHint": "API 金鑰提示",
    "aiAgent.apiKeyPlaceholder": "API 金鑰佔位",
    "aiAgent.systemPrompt": "系統提示",
    "aiAgent.systemPromptPlaceholder": "系統提示佔位",
    "aiAgent.temperature": "溫度",

    # browser
    "browser.closeBrowser": "關閉瀏覽器",
    "browser.connecting": "連線中",
    "browser.controlling": "控制中",
    "browser.deny": "拒絕",
    "browser.grant": "授權",
    "browser.idleWarning": "閒置警告",
    "browser.interactToKeep": "操作以保持連線",
    "browser.liveView": "即時預覽",
    "browser.releaseControl": "釋放控制",
    "browser.requestControl": "請求控制",
    "browser.requestsControl": "請求控制中",
    "browser.viewOnly": "僅檢視",
    "browser.viewing": "檢視中",
    "browser.waitingForStream": "等待串流中",

    # cloudTrial
    "cloudTrial.daysRemaining": "剩餘天數",
    "cloudTrial.expired": "已過期",
    "cloudTrial.navBadge": "導覽標記",
    "cloudTrial.planLabel": "方案名稱",
    "cloudTrial.trialActive": "試用啟用中",
    "cloudTrial.upgrade": "升級",

    # collaboration
    "collaboration.chat.empty": "尚無訊息",
    "collaboration.chat.placeholder": "輸入訊息...",
    "collaboration.connecting": "連線中",
    "collaboration.endSession": "結束工作階段",
    "collaboration.endSessionConfirm": "確定要結束此工作階段嗎？",
    "collaboration.invite.confirmJoin": "確認加入",
    "collaboration.invite.joinWorkflow": "加入工作流程",
    "collaboration.invite.step3Approve": "審核加入請求",
    "collaboration.invite.step4Collab": "開始協作",
    "collaboration.notConnected": "未連線",
    "collaboration.terminated": "已終止",

    # common
    "common.addItem": "新增項目",
    "common.decline": "拒絕",
    "common.moveDown": "下移",
    "common.moveUp": "上移",
    "common.none": "無",

    # code.*
    "code.autofix.statusPRPill": "PR #{n}",
    "code.dast.restApi": "REST API",
    "code.item.iacScan": "IaC",
    "code.login.google": "Google",
    "code.section.cicd": "CI/CD",

    # credentials
    "credentials.types.oauth2": "OAuth2",

    # dashboardPage
    "dashboardPage.devices.removed": "已移除",
    "data.tokensLabel": "令牌數",

    # landing pages
    "landing.about.faq.answer1": "Flyto 是一個開源自動化平台，可在伺服器、桌面和物聯網裝置上執行工作流程。",
    "landing.about.faq.answer2": "是的，Flyto 完全免費且開源，採用 MIT 授權。",
    "landing.about.faq.answer3": "Flyto 支援 Node.js 和 WebAssembly 執行環境。",
    "landing.about.faq.answer4": "支援 Windows、macOS 和 Linux，以及 Docker 容器。",
    "landing.about.faq.question1": "什麼是 Flyto？",
    "landing.about.faq.question2": "Flyto 是免費的嗎？",
    "landing.about.faq.question3": "Flyto 支援哪些程式語言？",
    "landing.about.faq.question4": "Flyto 支援哪些平台？",
    "landing.about.stats.atomicModules.label": "原子模組",
    "landing.about.stats.atomicModules.number": "384+",
    "landing.about.stats.enterpriseReady.label": "企業就緒",
    "landing.about.stats.enterpriseReady.number": "數字",
    "landing.about.stats.offlineCapable.label": "離線支援",
    "landing.about.stats.offlineCapable.number": "100%",

    # landing code/common
    "landing.code.automateAnything": "自動化一切",
    "landing.code.byCategory": "依分類",
    "landing.code.connectTo": "連接至",
    "landing.code.easyIntegration": "輕鬆整合",
    "landing.code.exploreModules": "探索模組",
    "landing.code.forDevelopers": "為開發者設計",
    "landing.code.getStarted": "開始使用",
    "landing.code.howItWorks": "運作方式",
    "landing.code.joinCommunity": "加入社群",
    "landing.code.learnMore": "了解更多",
    "landing.code.openSource": "開放原始碼",
    "landing.code.powerful": "功能強大",
    "landing.code.searchModules": "搜尋模組",
    "landing.code.simpleSetup": "簡單設定",
    "landing.code.startBuilding": "開始建構",
    "landing.code.viewDocs": "查看文件",
    "landing.code.viewOnGithub": "在 GitHub 上查看",

    "landing.common.getStarted": "開始使用",
    "landing.common.learnMore": "了解更多",
    "landing.common.tryForFree": "免費試用",
    "landing.common.viewDocs": "查看文件",
    "landing.common.watchDemo": "觀看示範",
    "landing.common.contactUs": "聯絡我們",
    "landing.common.signUp": "註冊",
    "landing.common.signIn": "登入",
    "landing.common.features": "功能特色",
    "landing.common.pricing": "方案價格",
    "landing.common.about": "關於",
    "landing.common.blog": "部落格",
    "landing.common.docs": "文件",
    "landing.common.support": "支援",
    "landing.common.community": "社群",
    "landing.common.changelog": "更新日誌",
    "landing.common.status": "系統狀態",
    "landing.common.terms": "服務條款",
    "landing.common.privacy": "隱私權政策",
    "landing.common.readMore": "閱讀更多",
    "landing.common.backToTop": "回到頂部",
    "landing.common.allRightsReserved": "版權所有",
    "landing.common.copyright": "版權聲明",
    "landing.common.madeWith": "以",
    "landing.common.and": "和",
    "landing.common.in": "在",

    # landing compare/overview/download/languagepacks
    "landing.compare.title": "比較方案",
    "landing.compare.subtitle": "選擇最適合您的方案",
    "landing.compare.feature": "功能",
    "landing.compare.free": "免費版",
    "landing.compare.pro": "專業版",
    "landing.compare.enterprise": "企業版",
    "landing.compare.included": "已包含",
    "landing.compare.notIncluded": "未包含",
    "landing.compare.custom": "自訂",
    "landing.compare.unlimited": "無限制",
    "landing.compare.contactSales": "聯絡業務",
    "landing.compare.startFree": "免費開始",
    "landing.compare.getStarted": "開始使用",
    "landing.compare.perMonth": "每月",
    "landing.compare.perYear": "每年",

    "landing.overview.title": "產品總覽",
    "landing.overview.subtitle": "一站式安全自動化平台",
    "landing.overview.feature1": "工作流程自動化",
    "landing.overview.feature2": "安全掃描",
    "landing.overview.feature3": "API 整合",
    "landing.overview.feature4": "即時監控",
    "landing.overview.description1": "視覺化拖放工作流程編輯器",
    "landing.overview.description2": "自動弱點掃描與修復建議",
    "landing.overview.description3": "384+ 模組連接各種服務",
    "landing.overview.description4": "遙測、告警與 AI 分析",

    "landing.download.title": "下載",
    "landing.download.subtitle": "選擇您的平台",
    "landing.download.desktop": "桌面版",
    "landing.download.server": "伺服器版",
    "landing.download.docker": "Docker 版",
    "landing.download.requirements": "系統需求",

    "landing.languagepacks.title": "語言包",
    "landing.languagepacks.subtitle": "多語言支援",
    "landing.languagepacks.available": "可用語言",
    "landing.languagepacks.community": "社群翻譯",
    "landing.languagepacks.contribute": "貢獻翻譯",
    "landing.languagepacks.coverage": "翻譯覆蓋率",
    "landing.languagepacks.download": "下載語言包",
    "landing.languagepacks.howToContribute": "如何貢獻",
    "landing.languagepacks.installGuide": "安裝指南",
    "landing.languagepacks.official": "官方語言",
    "landing.languagepacks.supported": "支援的語言",

    # scheduler
    "scheduler.detail.cronExpression": "Cron 表達式",
    "scheduler.detail.editSchedule": "編輯排程",
    "scheduler.detail.executionHistory": "執行歷史",
    "scheduler.detail.interval": "間隔",
    "scheduler.detail.lastExecution": "上次執行",
    "scheduler.detail.nextExecution": "下次執行",
    "scheduler.detail.scheduleDetails": "排程詳細資訊",
    "scheduler.detail.scheduleInfo": "排程資訊",
    "scheduler.detail.scheduleName": "排程名稱",
    "scheduler.detail.scheduleType": "排程類型",
    "scheduler.detail.triggerNow": "立即觸發",
    "scheduler.detail.updateSchedule": "更新排程",
    "scheduler.detail.workflow": "工作流程",
    "scheduler.detail.workflowName": "工作流程名稱",
    "scheduler.errors.createFailed": "建立排程失敗",
    "scheduler.errors.deleteFailed": "刪除排程失敗",
    "scheduler.errors.updateFailed": "更新排程失敗",
    "scheduler.stats.averageDuration": "平均持續時間",
    "scheduler.stats.successRate": "成功率",
    "scheduler.stats.totalExecutions": "總執行數",

    # recorder/rpa
    "recorder.elementSelector.highlight": "高亮顯示",
    "recorder.elementSelector.inspect": "檢查",
    "recorder.elementSelector.pick": "選取",
    "recorder.elementSelector.selector": "選擇器",
    "recorder.elementSelector.xpath": "XPath",

    # templateBuilder
    "templateBuilder.aiChat.analyzing": "分析中...",
    "templateBuilder.aiChat.askAnything": "詢問任何問題",
    "templateBuilder.aiChat.generating": "產生中...",
    "templateBuilder.aiChat.placeholder": "輸入您的問題...",
    "templateBuilder.aiChat.sendMessage": "發送訊息",
    "templateBuilder.aiChat.thinking": "思考中...",
    "templateBuilder.messages.workflowLocked": "此工作流程已鎖定，無法編輯。",

    # usage
    "usage.status.executions": "執行次數",
    "usage.status.limit": "上限",
    "usage.status.remaining": "剩餘",
    "usage.status.used": "已使用",

    # plugins
    "plugins.sort.alphabetical": "依字母排序",
    "plugins.sort.newest": "最新",
    "plugins.sort.popular": "最受歡迎",

    # misc cloud
    "cloud.outputs.label": "輸出",
    "cloud.outputs.noOutputs": "無輸出",
    "cloud.outputs.outputName": "輸出名稱",
    "cloud.templateBuilder.nodeProperties.foreachPlaceholder": "${'$'}{'{'}previous_step.items{'}'}",
}

# Apply translations
for scope in ['cloud', 'code', 'landing', 'app', 'console', 'data']:
    zh_dir = ROOT / 'locales' / scope / 'zh-TW'
    if not zh_dir.exists():
        continue
    for f in sorted(zh_dir.rglob('*.json')):
        with open(f, encoding='utf-8') as fh:
            data = json.load(fh)

        updated = 0
        for k, v in data.get('translations', {}).items():
            if k in ZH and data['translations'][k] != ZH[k]:
                data['translations'][k] = ZH[k]
                updated += 1

        if updated:
            with open(f, 'w', encoding='utf-8') as fh:
                json.dump(data, fh, indent=2, ensure_ascii=False)
                fh.write('\n')

# Count remaining
en_vals = {}
zh_vals = {}
for scope in ['cloud', 'code', 'landing', 'app', 'console', 'data']:
    for f in (ROOT / 'locales' / scope / 'en').rglob('*.json'):
        with open(f, encoding='utf-8') as fh:
            for k, v in json.load(fh).get('translations', {}).items():
                en_vals[k] = v
    zh_dir = ROOT / 'locales' / scope / 'zh-TW'
    if not zh_dir.exists(): continue
    for f in zh_dir.rglob('*.json'):
        with open(f, encoding='utf-8') as fh:
            for k, v in json.load(fh).get('translations', {}).items():
                zh_vals[k] = v

same = sum(1 for k in zh_vals if zh_vals[k] == en_vals.get(k, '') and en_vals.get(k, ''))
print(f'zh-TW still = English: {same}')
