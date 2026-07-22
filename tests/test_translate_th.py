"""Regression tests for the path-safe historical Thai translation batch."""

import json
import tempfile
import unittest
from pathlib import Path

import translate_th


class ThaiBatchTests(unittest.TestCase):
    """Verify the historical Thai batch is path-safe and dry-run aware."""

    def test_dry_run_reports_without_writing(self):
        """Leave the selected catalog unchanged while reporting fillable keys."""
        key, value = next(iter(translate_th.translations_th.items()))
        payload = {"translations": {key: ""}}
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "code.json"
            original = json.dumps(payload)
            path.write_text(original, encoding="utf-8")
            updated, missing, remaining = translate_th.apply_translations(path, dry_run=True)

            self.assertEqual(path.read_text(encoding="utf-8"), original)

        self.assertEqual(updated, 1)
        self.assertEqual(remaining, [])
        self.assertGreater(len(missing), 0)
        self.assertEqual(value, translate_th.translations_th[key])


if __name__ == "__main__":
    unittest.main()
