"""Regression coverage for the Flyto2 AI Space translation catalog."""

import json
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CATALOG_ROOT = PROJECT_ROOT / "locales" / "cloud"
OFFICIAL_LOCALES = ("en", "zh-TW", "zh-CN")
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
