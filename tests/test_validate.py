import json
import tempfile
import unittest
from pathlib import Path

from scripts.validate import validate_file


class ValidateCriticalTranslationsTests(unittest.TestCase):
    def _validate(self, value: str):
        payload = {
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
        errors = self._validate('')

        self.assertIn('missing_critical_translation', {error['type'] for error in errors})

    def test_accepts_translated_community_product_loop_copy(self):
        self.assertEqual(self._validate('驗證完整 CE 產品閉環'), [])


if __name__ == '__main__':
    unittest.main()
