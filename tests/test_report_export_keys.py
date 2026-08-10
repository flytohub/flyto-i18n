"""Contract tests for the Flyto2 report export format copy."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STALE_DIST_HINT = (
    "export copy differs between locales/ and dist/ — "
    "run `python3 scripts/build-dist.py` to rebuild the published bundles"
)
REQUIRED_KEYS = {
    "code.reports.chooseExportFormat",
    "code.reports.exportPptx",
}
REVIEWED_COPY = {
    "en": {
        "code.reports.chooseExportFormat": "Choose export format",
        "code.reports.exportPptx": "PowerPoint (.pptx)",
    },
    "zh-TW": {
        "code.reports.chooseExportFormat": "選擇匯出格式",
        "code.reports.exportPptx": "PowerPoint（.pptx）",
    },
    "zh-CN": {
        "code.reports.chooseExportFormat": "选择导出格式",
        "code.reports.exportPptx": "PowerPoint（.pptx）",
    },
}


def flatten(obj, prefix=""):
    """Flatten a generated translation object to dotted catalog keys."""
    result = {}
    for key, value in obj.items():
        full_key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            result.update(flatten(value, full_key))
        else:
            result[full_key] = value
    return result


def load_published(locale):
    """Read the built dist bundle for one code locale."""
    path = ROOT / "dist" / "code" / f"{locale}.json"
    return flatten(json.loads(path.read_text(encoding="utf-8"))["translations"])


class ReportExportTranslationTests(unittest.TestCase):
    """Keep report export labels present in source and published bundles."""

    def test_every_code_locale_publishes_non_empty_export_copy(self):
        """Require the format menu to remain usable in every supported locale."""
        locale_root = ROOT / "locales" / "code"
        locale_files = sorted(locale_root.glob("*/code.json"))
        self.assertEqual(16, len(locale_files))

        for path in locale_files:
            locale = path.parent.name
            with self.subTest(locale=locale):
                source = json.loads(path.read_text(encoding="utf-8"))["translations"]
                published = load_published(locale)
                for catalog in (source, published):
                    self.assertEqual(set(), REQUIRED_KEYS - catalog.keys())
                    self.assertEqual(
                        set(),
                        {
                            key
                            for key in REQUIRED_KEYS
                            if not str(catalog.get(key, "")).strip()
                        },
                    )

    def test_reviewed_primary_locale_copy_does_not_drift(self):
        """Pin the reviewed English and Chinese product wording."""
        for locale, expected in REVIEWED_COPY.items():
            with self.subTest(locale=locale):
                source = json.loads(
                    (ROOT / "locales" / "code" / locale / "code.json").read_text(
                        encoding="utf-8"
                    )
                )["translations"]
                self.assertEqual(expected, {key: source[key] for key in REQUIRED_KEYS})
                # Reviewed wording is only shipped once dist/ carries it too, so
                # pin the published bundle as well — a non-empty but stale label
                # would otherwise satisfy the coverage test above.
                published = load_published(locale)
                self.assertEqual(
                    expected,
                    {key: published[key] for key in REQUIRED_KEYS},
                    STALE_DIST_HINT,
                )


if __name__ == "__main__":
    unittest.main()
