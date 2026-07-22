"""Regression tests for schema and critical-translation validation."""

import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate import validate_file


class ValidateCriticalTranslationsTests(unittest.TestCase):
    """Verify non-empty rules for critical Flyto2 Code copy."""

    def _validate(self, value: str):
        """Validate one temporary critical translation value."""
        payload = {
            '$schema': '../../../schema/locale.schema.json',
            'locale': 'zh-TW',
            'category': 'code',
            'version': '1.0.0',
            'translations': {'code.communityLoop.title': value},
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / 'code.json'
            path.write_text(json.dumps(payload), encoding='utf-8')
            return validate_file(path, {'code.communityLoop.title'})

    def test_rejects_empty_community_product_loop_copy(self):
        """Reject an empty critical community-loop translation."""
        errors = self._validate('')

        self.assertIn('missing_critical_translation', {error['type'] for error in errors})

    def test_accepts_translated_community_product_loop_copy(self):
        """Accept a non-empty localized community-loop translation."""
        self.assertEqual(self._validate('驗證完整 CE 產品閉環'), [])

    def test_rejects_catalog_missing_schema_metadata(self):
        """Reject a locale document that omits required schema metadata."""
        payload = {
            'locale': 'en',
            'category': 'code',
            'version': '1.0.0',
            'translations': {'code.example.title': 'Example'},
        }
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / 'code.json'
            path.write_text(json.dumps(payload), encoding='utf-8')
            errors = validate_file(path, set())

        self.assertIn('schema_error', {error['type'] for error in errors})


if __name__ == '__main__':
    unittest.main()
