#!/usr/bin/env python3
"""Audit placeholder-set parity between English and translated catalogs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from i18n_contract import PROJECT_DIRS  # noqa: E402


ROOT = SCRIPT_DIR.parent
LOCALES_DIR = ROOT / "locales"
PLACEHOLDER_RE = re.compile(r"\{\{?([A-Za-z_][A-Za-z0-9_.-]*)\}?\}")


def placeholder_names(value: str) -> set[str]:
    """Extract named single- or double-brace placeholders from a value."""
    return set(PLACEHOLDER_RE.findall(value))


def load_translations(project: str, locale: str) -> dict[str, str]:
    """Merge one project's locale catalogs for placeholder comparison."""
    translations: dict[str, str] = {}
    locale_dir = LOCALES_DIR / project / locale
    if not locale_dir.exists():
        return translations
    for path in sorted(locale_dir.glob("*.json")):
        data = json.loads(path.read_text(encoding="utf-8"))
        translations.update(data.get("translations", {}))
    return translations


def audit_placeholders(projects: list[str], locales: list[str] | None = None) -> list[dict]:
    """Return non-empty translations whose placeholder set differs from English."""
    findings: list[dict] = []
    for project in projects:
        english = load_translations(project, "en")
        project_dir = LOCALES_DIR / project
        if not english or not project_dir.exists():
            continue
        targets = locales or sorted(
            path.name for path in project_dir.iterdir() if path.is_dir() and path.name != "en"
        )
        for locale in targets:
            for key, value in load_translations(project, locale).items():
                if key not in english or not isinstance(value, str) or not value:
                    continue
                expected = placeholder_names(english[key])
                actual = placeholder_names(value)
                if expected == actual:
                    continue
                findings.append({
                    "project": project,
                    "locale": locale,
                    "key": key,
                    "expected": sorted(expected),
                    "actual": sorted(actual),
                })
    return findings


def main() -> int:
    """Report placeholder drift and optionally fail for remediation work."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", choices=PROJECT_DIRS, action="append")
    parser.add_argument("--locale", action="append")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    findings = audit_placeholders(args.project or PROJECT_DIRS, args.locale)
    if args.json:
        print(json.dumps({"count": len(findings), "findings": findings}, ensure_ascii=False, indent=2))
    else:
        print(f"placeholder mismatches: {len(findings)}")
        for finding in findings[:50]:
            print(
                f"- {finding['project']}/{finding['locale']} {finding['key']}: "
                f"expected={finding['expected']} actual={finding['actual']}"
            )
        if len(findings) > 50:
            print(f"... {len(findings) - 50} more; use --json for the complete report")
    return 1 if args.strict and findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
