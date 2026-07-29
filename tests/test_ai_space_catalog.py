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
    "aiSpace.workspace.spaces",
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
    assert len(english_keys) >= 220

    for locale, translations in catalogs.items():
        assert set(translations) == english_keys, locale
        assert all(value.strip() for value in translations.values()), locale
