"""Regression coverage for the Flyto2 AI Space translation catalog."""

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOT = PROJECT_ROOT / "locales" / "cloud"
DIST_ROOT = PROJECT_ROOT / "dist" / "cloud"
OFFICIAL_LOCALES = ("en", "zh-TW", "zh-CN")
REVIEWED_HIERARCHY_COPY = {
    "en": {
        "aiSpace.workspace.dialogProductHint": "Compose workflows, context and policy",
        "aiSpace.workspace.selectSpaceHint": (
            "Choose a Space to compose its workflows, context and optional adapters."
        ),
        "aiSpace.workspace.tabs.resources": "Resources",
        "myTemplates.newTemplate": "New workflow",
        "myTemplates.subtitle": "Build and manage reusable automation workflows",
        "myTemplates.title": "My Workflows",
    },
    "zh-TW": {
        "aiSpace.workspace.dialogProductHint": "組合工作流程、情境與治理策略",
        "aiSpace.workspace.selectSpaceHint": (
            "選擇一個 Space，組合其中的工作流程、情境與選用轉接器。"
        ),
        "aiSpace.workspace.tabs.resources": "資源",
        "myTemplates.newTemplate": "新增工作流程",
        "myTemplates.subtitle": "建立並管理可重用的自動化工作流程",
        "myTemplates.title": "我的工作流程",
    },
    "zh-CN": {
        "aiSpace.workspace.dialogProductHint": "组合工作流、上下文与治理策略",
        "aiSpace.workspace.selectSpaceHint": (
            "选择一个 Space，组合其中的工作流、上下文与可选适配器。"
        ),
        "aiSpace.workspace.tabs.resources": "资源",
        "myTemplates.newTemplate": "新建工作流",
        "myTemplates.subtitle": "创建并管理可复用的自动化工作流",
        "myTemplates.title": "我的工作流",
    },
}
REQUIRED_WORKSPACE_KEYS = {
    "aiSpace.workspace.addResources",
    "aiSpace.workspace.addWorkflows",
    "aiSpace.workspace.approvalOff",
    "aiSpace.workspace.approvalOn",
    "aiSpace.workspace.basicSafetyHint",
    "aiSpace.workspace.basicScopeHint",
    "aiSpace.workspace.dialogProductHint",
    "aiSpace.workspace.dialogProductTitle",
    "aiSpace.workspace.runningWorkflow",
    "aiSpace.workspace.spaces",
}
REQUIRED_CONTROL_KEYS = {
    "aiSpace.controls.acknowledged",
    "aiSpace.controls.activeWorkflow",
    "aiSpace.controls.captureKey",
    "aiSpace.controls.deadmanTimeout",
    "aiSpace.controls.heartbeat",
    "aiSpace.controls.pressKeyNow",
    "aiSpace.controls.runtimeAudit",
    "aiSpace.controls.runtimeConnected",
    "aiSpace.controls.runtimeConnecting",
    "aiSpace.controls.runtimeDisabled",
    "aiSpace.controls.runtimeOffline",
    "aiSpace.controls.runtimeReadyHint",
    "aiSpace.controls.runtimeSafeHint",
}
REQUIRED_RESOURCE_KEYS = {
    "aiSpace.resources.adapter",
    "aiSpace.resources.capabilities",
    "aiSpace.resources.contractHint",
    "aiSpace.resources.contractTitle",
    "aiSpace.resources.endpointTitle",
    "aiSpace.resources.healthTimeout",
    "aiSpace.resources.leaseTtl",
    "aiSpace.resources.missingOutput",
    "aiSpace.resources.noContracts",
    "aiSpace.resources.openInput",
    "aiSpace.resources.outputs",
    "aiSpace.resources.permissions",
    "aiSpace.resources.routingTitle",
    "aiSpace.workspace.adapterEndpoints",
    "aiSpace.workspace.featureRouting",
    "aiSpace.workspace.outputToInput",
    "aiSpace.workspace.tabs.routing",
    "aiSpace.workspace.typedOutput",
}
REQUIRED_GUARDED_DELIVERY_KEYS = {
    "aiSpace.delivery.containerLocked",
    "aiSpace.delivery.containerUnlocked",
    "aiSpace.delivery.eventCheckpointResumed",
    "aiSpace.delivery.eventContainerUnlocked",
    "aiSpace.delivery.eventHandoffCompleted",
    "aiSpace.delivery.eventHandoffStarted",
    "aiSpace.delivery.eventItemRejected",
    "aiSpace.delivery.eventItemVerified",
    "aiSpace.delivery.eventPreconditionRejected",
    "aiSpace.delivery.eventPreconditionVerified",
    "aiSpace.delivery.eventRecipientRejected",
    "aiSpace.delivery.eventRecipientVerified",
    "aiSpace.delivery.events",
    "aiSpace.delivery.gateCheckpoint",
    "aiSpace.delivery.gateItem",
    "aiSpace.delivery.gatePreconditions",
    "aiSpace.delivery.gateRecipient",
    "aiSpace.delivery.gateUnlock",
    "aiSpace.delivery.guardedEvidenceTitle",
    "aiSpace.delivery.guardedFailed",
    "aiSpace.delivery.guardedHint",
    "aiSpace.delivery.guardedTitle",
    "aiSpace.delivery.locked",
    "aiSpace.delivery.unlocked",
}


def load_ai_space_catalog(locale: str) -> dict[str, str]:
    """Load the authoritative AI Space source catalog for one locale."""
    catalog_path = CATALOG_ROOT / locale / "aiSpace.json"
    data = json.loads(catalog_path.read_text(encoding="utf-8"))

    assert data["locale"] == locale
    assert data["category"] == "cloud.aiSpace"
    return data["translations"]


def load_cloud_catalog(locale: str, category: str) -> dict[str, str]:
    """Load one authoritative Flyto Cloud source catalog."""
    catalog_path = CATALOG_ROOT / locale / f"{category}.json"
    return json.loads(catalog_path.read_text(encoding="utf-8"))["translations"]


def load_generated_cloud_catalog(locale: str) -> dict:
    """Load one generated nested Cloud runtime bundle."""
    catalog_path = DIST_ROOT / f"{locale}.json"
    return json.loads(catalog_path.read_text(encoding="utf-8"))["translations"]


def test_official_ai_space_catalogs_have_parity_and_no_empty_values():
    """Keep official AI Space catalogs complete, aligned, and non-empty."""
    catalogs = {
        locale: load_ai_space_catalog(locale) for locale in OFFICIAL_LOCALES
    }
    english_keys = set(catalogs["en"])

    assert REQUIRED_WORKSPACE_KEYS <= english_keys
    assert REQUIRED_CONTROL_KEYS <= english_keys
    assert REQUIRED_RESOURCE_KEYS <= english_keys
    assert REQUIRED_GUARDED_DELIVERY_KEYS <= english_keys
    assert len(english_keys) >= 340

    for locale, translations in catalogs.items():
        assert set(translations) == english_keys, locale
        assert all(value.strip() for value in translations.values()), locale


def test_reviewed_cloud_copy_preserves_the_workflow_first_hierarchy():
    """Pin workflow-first copy and keep its legacy namespace mirror aligned."""
    for locale, expected in REVIEWED_HIERARCHY_COPY.items():
        ai_space = load_ai_space_catalog(locale)
        my_templates = load_cloud_catalog(locale, "myTemplates")
        other = load_cloud_catalog(locale, "other")
        generated = load_generated_cloud_catalog(locale)

        for key, value in expected.items():
            if key.startswith("aiSpace."):
                assert ai_space[key] == value, (locale, key)
                generated_key = key.removeprefix("aiSpace.")
                generated_value = generated["aiSpace"]
                for part in generated_key.split("."):
                    generated_value = generated_value[part]
                assert generated_value == value, (locale, key, "dist")
                continue

            assert my_templates[key] == value, (locale, key)
            generated_key = key.removeprefix("myTemplates.")
            assert generated["myTemplates"][generated_key] == value, (
                locale,
                key,
                "dist",
            )
            legacy_key = f"cloud.{key}"
            assert other[legacy_key] == value, (locale, legacy_key)
