"""Regression coverage for Core module labels consumed by the Cloud canvas."""

import importlib.util
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BUILD_SCRIPT = ROOT / "scripts" / "build-dist.py"

EN_LABELS = {
    "modules.ai.tool.label": "AI Tool",
    "modules.api.github.create_pr.label": "Create GitHub Pull Request",
    "modules.api.github.list_repos.label": "List GitHub Repositories",
    "modules.api.tavily_search.label": "Web Search (Tavily)",
    "modules.auth.oauth2.label": "OAuth2 Token Exchange",
    "modules.browser.detect.label": "Smart Detect",
    "modules.data.dedup.label": "Deduplicate Records",
    "modules.data.validate_records.label": "Validate Records",
    "modules.http.batch.label": "HTTP Batch",
    "modules.http.paginate.label": "HTTP Paginate",
    "modules.http.session.label": "HTTP Session",
    "modules.http.webhook_wait.label": "Webhook Wait",
    "modules.mcp.recipe.label": "MCP Recipe",
    "modules.output.display.label": "Display Output",
    "modules.reverse.attach.label": "Attach Debugger",
    "modules.reverse.breakpoint.label": "Set/Remove Breakpoint",
    "modules.reverse.code.label": "Code Analysis",
    "modules.reverse.deobfuscate.label": "Deobfuscate Code",
    "modules.reverse.detach.label": "Detach Debugger",
    "modules.reverse.evaluate_on_call_frame.label": "Evaluate On Call Frame",
    "modules.reverse.get_call_frames.label": "Get Call Frames",
    "modules.reverse.hook.label": "Hook Function",
    "modules.reverse.network.label": "Network Initiator Tracing",
    "modules.reverse.request_breakpoint.label": "Set/Remove Request Breakpoint",
    "modules.reverse.resume.label": "Resume Execution",
    "modules.reverse.scripts.label": "Debugger Scripts",
    "modules.reverse.sourcemap.label": "Source Map Resolver",
    "modules.reverse.step.label": "Step Execution",
    "modules.reverse.wait_paused.label": "Wait for Pause",
    "modules.reverse.websocket.label": "WebSocket Capture",
    "modules.test.assert_status.label": "Assert Status",
    "modules.test.assert_timing.label": "Assert Timing",
    "modules.verification.discover.label": "Verification Discover",
    "modules.verification.generate_scenarios.label": "Verification Generate Scenarios",
    "modules.verification.report.label": "Verification Report",
    "modules.verification.run.label": "Verification Run",
    "modules.warroom.discover.label": "Warroom Discover",
    "modules.warroom.generate_scenarios.label": "Warroom Generate Scenarios",
    "modules.warroom.llm_review.label": "Warroom LLM Review",
    "modules.warroom.public_site_verify.label": "Warroom Public Site Verify",
    "modules.warroom.report.label": "Warroom Report",
    "modules.warroom.run.label": "Warroom Run",
}

ZH_TW_LABELS = {
    "modules.ai.tool.label": "AI 工具",
    "modules.api.github.create_pr.label": "建立 GitHub Pull Request",
    "modules.api.github.list_repos.label": "列出 GitHub 儲存庫",
    "modules.api.tavily_search.label": "網頁搜尋（Tavily）",
    "modules.auth.oauth2.label": "OAuth2 權杖交換",
    "modules.browser.detect.label": "智慧偵測",
    "modules.data.dedup.label": "資料去重",
    "modules.data.validate_records.label": "驗證資料列",
    "modules.http.batch.label": "HTTP 批次",
    "modules.http.paginate.label": "HTTP 分頁",
    "modules.http.session.label": "HTTP 工作階段",
    "modules.http.webhook_wait.label": "等待 Webhook",
    "modules.mcp.recipe.label": "MCP 配方",
    "modules.output.display.label": "顯示輸出",
    "modules.reverse.attach.label": "附加除錯器",
    "modules.reverse.breakpoint.label": "設定或移除中斷點",
    "modules.reverse.code.label": "程式碼分析",
    "modules.reverse.deobfuscate.label": "程式碼去混淆",
    "modules.reverse.detach.label": "解除附加除錯器",
    "modules.reverse.evaluate_on_call_frame.label": "在呼叫框架上求值",
    "modules.reverse.get_call_frames.label": "取得呼叫框架",
    "modules.reverse.hook.label": "攔截函式",
    "modules.reverse.network.label": "網路發起端追蹤",
    "modules.reverse.request_breakpoint.label": "設定或移除請求中斷點",
    "modules.reverse.resume.label": "繼續執行",
    "modules.reverse.scripts.label": "除錯器指令碼",
    "modules.reverse.sourcemap.label": "來源對應解析",
    "modules.reverse.step.label": "單步執行",
    "modules.reverse.wait_paused.label": "等待暫停",
    "modules.reverse.websocket.label": "WebSocket 擷取",
    "modules.test.assert_status.label": "驗證狀態",
    "modules.test.assert_timing.label": "驗證時間",
    "modules.verification.discover.label": "探索驗證目標",
    "modules.verification.generate_scenarios.label": "產生驗證情境",
    "modules.verification.report.label": "驗證報告",
    "modules.verification.run.label": "執行驗證",
    "modules.warroom.discover.label": "戰情室探索",
    "modules.warroom.generate_scenarios.label": "產生戰情室情境",
    "modules.warroom.llm_review.label": "戰情室 LLM 審查",
    "modules.warroom.public_site_verify.label": "公開網站驗證",
    "modules.warroom.report.label": "戰情室報告",
    "modules.warroom.run.label": "戰情室執行",
}

ZH_CN_LABELS = {
    "modules.ai.tool.label": "AI 工具",
    "modules.api.github.create_pr.label": "创建 GitHub Pull Request",
    "modules.api.github.list_repos.label": "列出 GitHub 仓库",
    "modules.api.tavily_search.label": "网页搜索（Tavily）",
    "modules.auth.oauth2.label": "OAuth2 令牌交换",
    "modules.browser.detect.label": "智能检测",
    "modules.data.dedup.label": "数据去重",
    "modules.data.validate_records.label": "验证数据行",
    "modules.http.batch.label": "HTTP 批处理",
    "modules.http.paginate.label": "HTTP 分页",
    "modules.http.session.label": "HTTP 会话",
    "modules.http.webhook_wait.label": "等待 Webhook",
    "modules.mcp.recipe.label": "MCP 配方",
    "modules.output.display.label": "显示输出",
    "modules.reverse.attach.label": "附加调试器",
    "modules.reverse.breakpoint.label": "设置或移除断点",
    "modules.reverse.code.label": "代码分析",
    "modules.reverse.deobfuscate.label": "代码去混淆",
    "modules.reverse.detach.label": "解除附加调试器",
    "modules.reverse.evaluate_on_call_frame.label": "在调用帧上求值",
    "modules.reverse.get_call_frames.label": "获取调用帧",
    "modules.reverse.hook.label": "拦截函数",
    "modules.reverse.network.label": "网络发起端追踪",
    "modules.reverse.request_breakpoint.label": "设置或移除请求断点",
    "modules.reverse.resume.label": "继续执行",
    "modules.reverse.scripts.label": "调试器脚本",
    "modules.reverse.sourcemap.label": "源映射解析",
    "modules.reverse.step.label": "单步执行",
    "modules.reverse.wait_paused.label": "等待暂停",
    "modules.reverse.websocket.label": "WebSocket 捕获",
    "modules.test.assert_status.label": "验证状态",
    "modules.test.assert_timing.label": "验证时间",
    "modules.verification.discover.label": "探索验证目标",
    "modules.verification.generate_scenarios.label": "生成验证场景",
    "modules.verification.report.label": "验证报告",
    "modules.verification.run.label": "执行验证",
    "modules.warroom.discover.label": "战情室探索",
    "modules.warroom.generate_scenarios.label": "生成战情室场景",
    "modules.warroom.llm_review.label": "战情室 LLM 审查",
    "modules.warroom.public_site_verify.label": "公开网站验证",
    "modules.warroom.report.label": "战情室报告",
    "modules.warroom.run.label": "战情室执行",
}


def load_build_module():
    """Load the distribution builder for source-to-bundle assertions."""
    spec = importlib.util.spec_from_file_location("build_dist_module_labels", BUILD_SCRIPT)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def source_values(locale: str) -> tuple[dict[str, str], dict[str, list[str]]]:
    """Return merged module copy and the files that own each key."""
    values: dict[str, str] = {}
    owners: dict[str, list[str]] = {}
    for path in sorted((ROOT / "locales" / "modules" / locale).glob("*.json")):
        translations = json.loads(path.read_text(encoding="utf-8"))["translations"]
        values.update(translations)
        for key in translations:
            owners.setdefault(key, []).append(path.name)
    return values, owners


def nested_value(payload: dict, dotted_key: str):
    """Resolve one dotted source key in a generated Vue i18n bundle."""
    current = payload
    for segment in dotted_key.split("."):
        current = current[segment]
    return current


def test_core_module_labels_are_reviewed_and_have_one_source_owner():
    """Pin the missing-label closure in all three official locales."""
    for locale, expected in {
        "en": EN_LABELS,
        "zh-TW": ZH_TW_LABELS,
        "zh-CN": ZH_CN_LABELS,
    }.items():
        values, owners = source_values(locale)
        assert {key: values[key] for key in expected} == expected
        assert all(owners[key] and len(owners[key]) == 1 for key in expected)


def test_core_module_labels_reach_the_cloud_distribution():
    """Require generated Cloud bundles to publish every reviewed label."""
    module = load_build_module()
    for locale, expected in {
        "en": EN_LABELS,
        "zh-TW": ZH_TW_LABELS,
        "zh-CN": ZH_CN_LABELS,
    }.items():
        translations = module.build_locale(locale, "cloud")["translations"]
        for key, value in expected.items():
            assert nested_value(translations, key) == value
