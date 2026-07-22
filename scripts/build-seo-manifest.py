#!/usr/bin/env python3
"""
build-seo-manifest.py - Build the Flyto2 public multilingual SEO contract.

The generated dist/seo-manifest.json gives landing/docs/blog the same locale,
hreflang, sitemap, and keyword-research contract without duplicating it in each
public site repository.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from i18n_contract import build_locale_meta, language_meta, locale_sort_key  # noqa: E402

PROJECT_ROOT = Path(__file__).parent.parent
CONTRACT_FILE = PROJECT_ROOT / "seo" / "public-surfaces.json"
DIST_DIR = PROJECT_ROOT / "dist"
OUTPUT_FILE = DIST_DIR / "seo-manifest.json"

REQUIRED_SURFACES = {"landing", "docs", "blog"}
REQUIRED_SIGNALS = {
    "canonical",
    "hreflang-alternates",
    "x-default",
    "sitemap",
    "localized-title",
    "localized-description",
}


def load_json(path: Path) -> dict:
    """Load a JSON file with UTF-8 encoding."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def discover_locales(locales_root: Path | None = None) -> list[str]:
    """Discover public locales from locales/cloud, the broadest shipped scope."""
    root = locales_root or PROJECT_ROOT / "locales" / "cloud"
    if not root.exists():
        return []
    return sorted([path.name for path in root.iterdir() if path.is_dir()], key=locale_sort_key)


def stable_hash(payload: dict) -> str:
    """Create a stable content hash for generated SEO manifests."""
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()[:12]


def locale_prefix(locale: str, default_locale: str) -> str:
    """Return the public path prefix for a locale."""
    if locale == default_locale:
        return ""
    return f"/{locale}"


def build_alternates(origin: str, locales: list[str], default_locale: str, x_default_locale: str) -> dict:
    """Build URL templates for localized alternates."""
    alternates = {}
    for locale in locales:
        meta = language_meta(locale)
        alternates[meta["hreflang"]] = f"{origin}{locale_prefix(locale, default_locale)}{{path}}"
    alternates["x-default"] = f"{origin}{locale_prefix(x_default_locale, default_locale)}{{path}}"
    return alternates


def validate_contract(contract: dict) -> list[str]:
    """Return contract validation errors."""
    errors = []
    surfaces = contract.get("surfaces", {})
    missing_surfaces = REQUIRED_SURFACES - set(surfaces)
    if missing_surfaces:
        errors.append(f"Missing public SEO surface(s): {', '.join(sorted(missing_surfaces))}")

    signals = set(contract.get("requiredSignals", []))
    missing_signals = REQUIRED_SIGNALS - signals
    if missing_signals:
        errors.append(f"Missing required signal(s): {', '.join(sorted(missing_signals))}")

    for surface_id, surface in sorted(surfaces.items()):
        origin = surface.get("origin", "")
        if not origin.startswith("https://") or "flyto2.com" not in origin:
            errors.append(f"{surface_id}: origin must be an https://*.flyto2.com URL")
        if not surface.get("sitemap", "").startswith(origin):
            errors.append(f"{surface_id}: sitemap must live under the surface origin")
        if "{path}" not in surface.get("routePattern", ""):
            errors.append(f"{surface_id}: routePattern must include {{path}}")
        clusters = surface.get("keywordClusters", [])
        if not clusters:
            errors.append(f"{surface_id}: at least one keyword cluster is required")
        for cluster in clusters:
            cluster_id = cluster.get("id", "<missing>")
            if not cluster.get("primary"):
                errors.append(f"{surface_id}.{cluster_id}: primary keyword is required")
            if not cluster.get("longTail"):
                errors.append(f"{surface_id}.{cluster_id}: longTail keywords are required")
            evidence = cluster.get("evidence", {})
            for field in ["source", "country", "language", "observedAt"]:
                if not evidence.get(field):
                    errors.append(f"{surface_id}.{cluster_id}: evidence.{field} is required")
    return errors


def build_seo_manifest(contract: dict, locales: list[str]) -> dict:
    """Build the distributable SEO manifest."""
    errors = validate_contract(contract)
    if errors:
        raise ValueError("\n".join(errors))

    default_locale = contract["defaultLocale"]
    x_default_locale = contract.get("xDefaultLocale", default_locale)
    locale_meta = build_locale_meta(locales)

    surfaces = {}
    for surface_id, surface in sorted(contract["surfaces"].items()):
        origin = surface["origin"].rstrip("/")
        surfaces[surface_id] = {
            "name": surface["name"],
            "origin": origin,
            "sitemap": surface["sitemap"],
            "routePattern": surface["routePattern"],
            "primaryIntent": surface["primaryIntent"],
            "requiredSignals": contract["requiredSignals"],
            "alternatesTemplate": build_alternates(origin, locales, default_locale, x_default_locale),
            "keywordClusters": surface["keywordClusters"],
        }

    manifest = {
        "version": "",
        "sourceVersion": contract["version"],
        "description": contract["description"],
        "defaultLocale": default_locale,
        "xDefaultLocale": x_default_locale,
        "locales": locale_meta["locales"],
        "surfaces": surfaces,
    }
    manifest["version"] = stable_hash(manifest)
    return manifest


def render_json(payload: dict) -> str:
    """Render JSON exactly as tracked in dist."""
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main() -> None:
    """Build or freshness-check the multilingual SEO manifest."""
    parser = argparse.ArgumentParser(description="Build dist/seo-manifest.json")
    parser.add_argument("--check", action="store_true", help="Fail if dist/seo-manifest.json is stale")
    args = parser.parse_args()

    contract = load_json(CONTRACT_FILE)
    locales = discover_locales()
    manifest = build_seo_manifest(contract, locales)
    rendered = render_json(manifest)

    if args.check:
        if not OUTPUT_FILE.exists() or OUTPUT_FILE.read_text(encoding="utf-8") != rendered:
            print("dist/seo-manifest.json is stale; run python3 scripts/build-seo-manifest.py")
            sys.exit(1)
        print("dist/seo-manifest.json is fresh")
        return

    DIST_DIR.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(rendered, encoding="utf-8")
    print(f"→ {OUTPUT_FILE.relative_to(PROJECT_ROOT)} ({len(locales)} locales, {len(manifest['surfaces'])} surfaces)")


if __name__ == "__main__":
    main()
