"""Regression tests for translation placeholder extraction."""

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "audit-placeholders.py"
FOOTPRINT_METRIC_PLACEHOLDERS = {
    "footprint.connector.outputLatency": {"outputs", "latency"},
    "footprint.run.entities": {"n"},
    "footprint.run.outputs": {"n"},
    "footprint.run.productiveSources": {"n"},
    "footprint.run.signals": {"n"},
    "footprint.run.tokens": {"n"},
}


def load_audit_module():
    """Load the hyphenated placeholder auditor as an isolated module."""
    spec = importlib.util.spec_from_file_location("audit_placeholders", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class PlaceholderAuditTests(unittest.TestCase):
    """Verify placeholder extraction across supported brace styles."""

    def setUp(self):
        """Load a fresh placeholder-audit module for each test."""
        self.module = load_audit_module()

    def test_extracts_single_and_double_brace_names(self):
        """Normalize single- and double-brace placeholders to name sets."""
        value = "Run {count} tasks with {{agent_name}} and ${workflow.id}"
        self.assertEqual(
            self.module.placeholder_names(value),
            {"count", "agent_name", "workflow.id"},
        )

    def test_ignores_plain_braces_without_identifiers(self):
        """Ignore incomplete or non-identifier brace content."""
        self.assertEqual(self.module.placeholder_names("Type ${ or use {two words}"), set())

    def test_footprint_metrics_are_localized_with_placeholder_parity(self):
        """Keep execution metrics usable and interpolatable in every Code locale."""
        code_root = SCRIPT_PATH.parents[1] / "locales" / "code"
        locales = sorted(path.name for path in code_root.iterdir() if path.is_dir())
        self.assertEqual(len(locales), 16)

        for locale in locales:
            catalog = self.module.load_translations("code", locale)
            for key, expected_placeholders in FOOTPRINT_METRIC_PLACEHOLDERS.items():
                with self.subTest(locale=locale, key=key):
                    self.assertIn(key, catalog)
                    self.assertTrue(catalog[key].strip())
                    self.assertEqual(
                        self.module.placeholder_names(catalog[key]),
                        expected_placeholders,
                    )


if __name__ == "__main__":
    unittest.main()
