# Tooling And Side Effects

Run scripts from the repository root with Python 3.11 or newer. Install pinned
dependencies first with `python3 -m pip install -r requirements.txt`.
The pinned toolchain includes JSON Schema validation, optional assisted
translation, and Ruff static analysis.

## Read-Only Checks

| Script | Interface |
| --- | --- |
| `validate.py` | `[-l locale] [-p project] [--strict]`; validates catalog shape and critical rules. Strict mode exits non-zero on errors. |
| `coverage.py` | `[-l locale] [-p project] [--json]`; reports unique-key completion. |
| `check_coverage.py` | `[--min percent] [--lang locale]`; legacy threshold check. |
| `build-seo-manifest.py --check` | Validates source and fails if the tracked SEO manifest is stale. |
| `generate-reference.py` | Fails when a Python declaration lacks a docstring or the tracked symbol reference is stale. |
| `audit-placeholders.py [--project scope] [--locale locale] [--json] [--strict]` | Compares non-empty translated placeholder sets with English. Default mode reports; strict mode exits non-zero on drift. |

## Deterministic Writers

| Script | Writes |
| --- | --- |
| `build-dist.py` | Rebuilds scoped and aggregate translation JSON plus locale metadata under `dist/`. |
| `build-seo-manifest.py` | Rebuilds `dist/seo-manifest.json`. |
| `build.py [-l locale] [-o dir]` | Legacy aggregate builder for a selected locale/output. Prefer `build-dist.py`. |
| `build-app.py` | Builds the mobile app locale form. |
| `add-locale.py locale [--with-english]` | Creates source directories/files for a locale; `--list` is read-only. |
| `sync-locales.py [--dry-run] [-l locale] [-p project]` | Adds missing English keys and removes obsolete keys in locale source. |
| `convert-tw-to-cn.py [--dry-run] [--force] [-p project]` | Uses OpenCC to derive Simplified Chinese source. Requires the OpenCC dependency. |
| `import-overrides.py source locale [--dry-run]` | Imports reviewed override values into locale source. |
| `split-cloud-translations.py [--cloud-path path] [--dry-run]` | Splits a Cloud translation source into repository catalogs. |
| `add-cloud-keys.py`, `add-code-keys.py`, `add_upstream_keys.py` | Maintenance migrations that add extracted upstream keys. Review diffs before retaining changes. |

## Cross-Repository Writers

| Script | Contract |
| --- | --- |
| `sync-from-core.py [--core-path path] [--dry-run] [--delete-stale]` | Scans Core module schemas and updates module locale source. Unscanned keys are preserved unless destructive mode is explicit. |
| `sync-from-cloud.py [--cloud-path path] [--dry-run] [--delete-stale]` | Scans Cloud `$t()` calls and updates Cloud locale source. Unscanned keys are preserved unless destructive mode is explicit. |
| `sync-to-projects.py [--dry-run] [--project cloud|code|app]` | Copies generated bundles to sibling consumers and can delete stale target locale files. |
| `install-hooks.sh` | Installs local Git hooks; inspect before running because it changes `.git/hooks`. |

## Networked Assisted Translation

`translate-with-openai.py --target locale` accepts optional `--project`,
`--file`, `--force`, `--untranslated`, `--dry-run`, and `--model`. Non-dry runs
can call OpenAI and write translated source files. It reads `OPENAI_API_KEY`
from the environment and may incur API cost. Never run it against sensitive
content or merge its output without human review.

## Internal Migration Helpers

`_apply_manual_translations.py`, `_apply_saved_locally.py`, and
`_apply_stalled_scan.py` are one-off maintenance helpers, not stable user APIs.
Read their constants and target paths before use, run them only in a disposable
branch, and validate/rebuild all output afterward.

`scripts/one-off/` contains additional historical migrations. The root
`translate_th.py [--path catalog] [--dry-run]` is retained for compatibility
with one reviewed Thai batch; it defaults to the repository catalog and never
writes during import.

## Source API Reference

[The generated Python symbol reference](generated/python-symbols.md) covers all
188 declarations under `scripts/` and `tests/`, including nested helpers,
historical one-off migrations, test fixtures, and CLI entry points. The source
docstring is the method contract; the generated table is the navigation and
drift-check layer. Run `npm run docs:write` after an intentional declaration or
docstring change.

Placeholder parity is audited separately because the repository has a measured
legacy baseline of 577 mismatches across all community and official catalogs.
The standard verify gate reports schema, injection, corrupt replacement, and
critical-copy violations; use `npm run audit:placeholders` for the complete
placeholder remediation inventory and `--strict` only in a scoped cleanup.
