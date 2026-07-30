"""Contract tests for durable footprint-run status copy."""

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_KEYS = (
    "code.footprint.run.diagnosticsTitle",
    "code.footprint.run.initializingSchedule",
    "code.footprint.run.queued",
    "code.footprint.run.queuedTitle",
    "code.footprint.run.waitingWorker",
)


class FootprintDurableRunTranslationTests(unittest.TestCase):
    """Keep worker and queue state truthful in every supported locale."""

    def test_required_keys_are_non_empty_in_every_code_locale(self):
        """Require durable queue-state copy to be non-empty in every Code locale."""
        locale_files = sorted((ROOT / "locales" / "code").glob("*/code.json"))
        self.assertGreater(len(locale_files), 0)

        for path in locale_files:
            payload = json.loads(path.read_text(encoding="utf-8"))
            translations = payload["translations"]
            for key in REQUIRED_KEYS:
                with self.subTest(locale=path.parent.name, key=key):
                    value = translations.get(key)
                    self.assertIsInstance(value, str)
                    self.assertTrue(value.strip())


if __name__ == "__main__":
    unittest.main()
