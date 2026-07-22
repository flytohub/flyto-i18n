"""Regression tests for multilingual SEO contract generation."""

import importlib.util
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "build-seo-manifest.py"


def load_seo_module():
    """Load the hyphenated SEO builder as an isolated test module."""
    spec = importlib.util.spec_from_file_location("build_seo_manifest", SCRIPT_PATH)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


class BuildSeoManifestTests(unittest.TestCase):
    """Verify SEO surface expansion and source-contract rejection paths."""

    def setUp(self):
        """Create a valid three-surface SEO source contract."""
        self.module = load_seo_module()
        self.contract = {
            "version": "test",
            "description": "Test SEO contract",
            "defaultLocale": "en",
            "xDefaultLocale": "en",
            "requiredSignals": [
                "canonical",
                "hreflang-alternates",
                "x-default",
                "sitemap",
                "localized-title",
                "localized-description",
                "og-locale",
                "structured-data",
            ],
            "surfaces": {
                "landing": self.surface("https://flyto2.com"),
                "docs": self.surface("https://docs.flyto2.com"),
                "blog": self.surface("https://blog.flyto2.com"),
            },
        }

    def surface(self, origin: str) -> dict:
        """Build one valid public-surface fixture for an origin."""
        return {
            "name": origin,
            "origin": origin,
            "sitemap": f"{origin}/sitemap.xml",
            "routePattern": "/{locale}{path}",
            "primaryIntent": "test",
            "keywordClusters": [
                {
                    "id": "cluster",
                    "primary": "ai workflow automation",
                    "intent": "test",
                    "evidence": {
                        "source": "test",
                        "country": "US",
                        "language": "en",
                        "observedAt": "2026-07-18",
                    },
                    "longTail": ["open source workflow automation"],
                }
            ],
        }

    def test_builds_three_public_surfaces_with_x_default(self):
        """Generate locale alternates, x-default, and Open Graph metadata."""
        manifest = self.module.build_seo_manifest(self.contract, ["en", "zh-TW", "ja"])

        self.assertEqual(set(manifest["surfaces"]), {"landing", "docs", "blog"})
        landing_alternates = manifest["surfaces"]["landing"]["alternatesTemplate"]
        self.assertEqual(landing_alternates["en"], "https://flyto2.com{path}")
        self.assertEqual(landing_alternates["zh-TW"], "https://flyto2.com/zh-TW{path}")
        self.assertEqual(landing_alternates["x-default"], "https://flyto2.com{path}")
        self.assertEqual(manifest["locales"]["ja"]["og_locale"], "ja_JP")
        self.assertTrue(manifest["version"])

    def test_rejects_missing_public_surface(self):
        """Reject a source contract missing a required public surface."""
        del self.contract["surfaces"]["blog"]

        with self.assertRaises(ValueError) as ctx:
            self.module.build_seo_manifest(self.contract, ["en"])

        self.assertIn("Missing public SEO surface", str(ctx.exception))

    def test_rejects_keyword_cluster_without_evidence_source(self):
        """Reject keyword research without a named evidence source."""
        cluster = self.contract["surfaces"]["docs"]["keywordClusters"][0]
        cluster["evidence"]["source"] = ""

        with self.assertRaises(ValueError) as ctx:
            self.module.build_seo_manifest(self.contract, ["en"])

        self.assertIn("evidence.source", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
