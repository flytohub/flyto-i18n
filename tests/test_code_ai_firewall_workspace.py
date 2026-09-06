"""Source-owned AI Firewall workspaces, safety semantics and bundle parity."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = "agentFirewall.workspace."


def flatten(node, prefix=""):
    """Return comparable dot keys from a generated distribution bundle."""
    result = {}
    for key, value in node.items():
        full = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten(value, full))
        elif isinstance(value, str):
            result[full.removesuffix("._self")] = value
    return result


def test_workspace_sources_and_generated_distributions():
    """All supported locales retain one source owner and exact generated copy."""
    expected = None
    for source in sorted((ROOT / "locales/code").glob("*/code.json")):
        locale = source.parent.name
        translations = json.loads(source.read_text())["translations"]
        keys = {key for key in translations if key.startswith(PREFIX)}
        assert len(keys) == 57
        if expected is None:
            expected = keys
        assert keys == expected
        for artifact in [ROOT / "dist/code" / f"{locale}.json", ROOT / "dist" / f"{locale}.json"]:
            bundle = flatten(json.loads(artifact.read_text())["translations"])
            for key in keys:
                assert translations[key].strip()
                assert "{{" not in translations[key]
                assert bundle.get(key, bundle.get("code." + key)) == translations[key]
        for key in keys:
            owners = [p for p in source.parent.glob("*.json") if key in json.loads(p.read_text()).get("translations", {})]
            assert owners == [source], (key, owners)


def test_workspace_evidence_and_placeholder_contract():
    """Safety-critical distinctions and formatting slots survive localization."""
    catalogs = {locale: json.loads((ROOT / "locales/code" / locale / "code.json").read_text())["translations"] for locale in ["en", "zh-TW"]}
    en = catalogs["en"]
    assert "not proof of successful execution" in en[PREFIX + "historicalLimit"]
    assert "not completed tests" in en[PREFIX + "scenarioLimit"]
    assert "do not release an individual held tool call" in en[PREFIX + "approvalScope"]
    assert "does not establish" in en[PREFIX + "noSimulation"]
    assert en[PREFIX + "decision.unknown"] == "Not recorded"
    assert en[PREFIX + "decision.approval"] != en[PREFIX + "decision.held"]
    for key in en:
        if key.startswith(PREFIX):
            assert set(re.findall(r"\{\w+\}", en[key])) == set(re.findall(r"\{\w+\}", catalogs["zh-TW"][key]))
