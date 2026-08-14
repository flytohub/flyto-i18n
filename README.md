# Flyto2 i18n

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Website](https://img.shields.io/badge/website-flyto2.com-8B5CF6)](https://flyto2.com)
[![Docs](https://img.shields.io/badge/docs-docs.flyto2.com-06B6D4)](https://docs.flyto2.com)

Fix a translation once and share it across every Flyto2 product, docs, and website surface.

The same product copy drifts across many Flyto2 repositories and locales. This
repository owns the reviewed translation source and generates the bundles that
consumers use, so the fix does not need to be copied into each repository.

## Quick Start: Fix a Translation

Edit the value in its existing source catalog, then validate and rebuild the
tracked bundles:

`locales/code/ja/code.json`:

```json
{
    "translations": {
        "code.approval.approve": "承認"
    }
}
```

```bash
python3 scripts/validate.py --strict
python3 scripts/build-dist.py
```

Submit the source and generated `dist/` changes together. Once merged and
published, each consuming surface receives the fix through its configured CDN
refresh or bundled-artifact deployment.

You can also make the same source edit in GitHub and submit a pull request; the
repository workflows validate and rebuild the tracked bundles.

## What This Repository Owns

The translation catalogs and generated runtime bundles cover Flyto2 Cloud,
Code, Console, Data, Engine, App, Landing, shared copy, and Flyto2 Core modules.
The repository also owns shared locale metadata and the multilingual SEO
contract consumed by the Flyto2 website, docs, and blog.

Official links: [flyto2.com](https://flyto2.com) ·
[Docs](https://docs.flyto2.com) ·
[Blog](https://blog.flyto2.com) ·
[Contributing](CONTRIBUTING.md) ·
[Security](mailto:security@flyto2.com)

## Architecture

```
You edit source data      Build refreshes dist/      Public surfaces consume it
─────────────────── ──▶ ─────────────────── ──▶ ─────────────────────────────
locales/code/ja/        dist/code/ja.json        Runtime translation bundle
seo/public-surfaces     dist/seo-manifest.json   SEO/hreflang contract
```

Flyto2 Cloud, Code, Console, Data, Engine, App, and Landing consume generated
`dist/` bundles. Public sites can also consume `dist/locale-meta.json` and
`dist/seo-manifest.json` for shared locale, hreflang, sitemap, Open Graph
locale, and long-tail keyword contract data.

Connected Flyto2 apps load translations from CDN at runtime. Flyto2 Flow is the
offline exception: CI or the Docker build syncs `dist/flow` and local flag SVGs
into the application image, so it performs no runtime CDN request.

## Quick Start: Add a New Language

```bash
# 1. Clone and run the add-locale script
git clone https://github.com/flytohub/flyto-i18n.git
cd flyto-i18n
python3 -m pip install -r requirements.txt
python scripts/add-locale.py <locale-code>   # e.g. "ru" for Russian

# 2. Translate — fill in the empty values in locales/*/<locale-code>/
#    (all keys are pre-created with "" placeholder)

# 3. Add a flag SVG to dist/flags/<region>.svg (circle-flag style, 512x512)

# 4. Validate
python scripts/validate.py --locale <locale-code>

# 5. Build & preview
python scripts/build-dist.py
python scripts/build-seo-manifest.py

# 6. Submit PR
```

Once merged, the new locale becomes available in the published metadata and
bundles. Each consuming app must still enable the locale in its own release or
runtime picker contract.

## File Structure

```
locales/
├── cloud/{locale}/*.json     # Flyto2 Cloud (automation platform)
├── code/{locale}/*.json      # Flyto2 Code (war room)
├── modules/{locale}/*.json   # Flyto2 Core (workflow modules)
├── landing/{locale}/*.json   # Landing page & marketing
├── shared/{locale}/*.json    # Common translations (shared across apps)
├── app/{locale}/*.json       # Flutter mobile app
├── console/{locale}/*.json   # Flyto2 Console
├── data/{locale}/*.json      # Flyto2 Data
└── engine/{locale}/*.json    # Flyto2 Engine runtime messages

seo/
└── public-surfaces.json      # Landing/docs/blog SEO, sitemap, and keyword contract

dist/                         # Auto-generated, served via CDN
├── {scope}/{locale}.json     # Merged + nested (what apps actually load)
├── {scope}/manifest.json     # Locale metadata (completion %, region)
├── locale-meta.json          # Flags, region, hreflang, og_locale, direction
├── seo-manifest.json         # Public SEO contract for landing/docs/blog
└── flags/*.svg               # Country flag icons (21 flags)
```

## Translation File Format

```json
{
    "$schema": "../../../schema/locale.schema.json",
    "locale": "ja",
    "category": "code",
    "version": "1.0.0",
    "translations": {
        "code.nav.dashboard": "ダッシュボード",
        "code.nav.repos": "リポジトリ",
        "code.nav.issues": "セキュリティ問題"
    }
}
```

Rules:
- Keys are dot-separated: `{scope}.{section}.{name}`
- Values must be no more than 800 characters
- Use `{n}`, `{name}` for variables (not `${...}`)
- Empty `""` = untranslated (app falls back to English automatically)

## Supported Languages

| Locale | Language | Status | Overall dist coverage |
|--------|----------|--------|----------|
| en | English | Official | 99.2% |
| zh-TW | 繁體中文 | Official | 98.1% |
| zh-CN | 简体中文 | Official | 97.6% |
| ja | 日本語 | Official | 87.8% |
| id | Bahasa Indonesia | Community | 77.6% |
| it | Italiano | Community | 77.6% |
| pl | Polski | Community | 77.6% |
| ko | 한국어 | Community | 77.1% |
| fr | Français | Community | 77.1% |
| es | Español | Community | 77.1% |
| de | Deutsch | Community | 77.1% |
| pt-BR | Português (Brasil) | Community | 77.1% |
| vi | Tiếng Việt | Community | 77.1% |
| th | ภาษาไทย | Community | 77.1% |
| hi | हिन्दी | Community | 77.1% |
| tr | Türkçe | Community | 77.1% |

Coverage is generated from unique merged keys in `dist/manifest.json`. Per-scope
coverage lives in `dist/{scope}/manifest.json`; landing, app, console, data, and
engine are currently complete, while code translations still need the most work.

## Multilingual SEO Contract

`seo/public-surfaces.json` is the source of truth for the three public Flyto2
surfaces:

- `landing`: `https://flyto2.com`
- `docs`: `https://docs.flyto2.com`
- `blog`: `https://blog.flyto2.com`

It records required SEO signals, sitemap URLs, route templates, keyword intent,
long-tail terms, and observed search metrics. `scripts/build-seo-manifest.py`
turns that source into `dist/seo-manifest.json`, including:

- locale metadata for 16 shipped locales
- `hreflang` alternate URL templates plus `x-default`
- `og_locale` values for social previews
- public-surface sitemap locations
- keyword clusters for product, docs, and blog content planning

Public sites should use this manifest when generating canonical URLs,
alternate language links, sitemaps, localized metadata, and AI-search/LLM
citation text.

## CI/CD Pipeline

The checked-in workflows have distinct responsibilities:

| Workflow | Trigger | Contract |
|------|------|-------------|
| `validate.yml` | Every main push and pull request | Compiles scripts, validates catalogs, runs unit tests, builds distributions, and runs the Flyto2 indexer gate. |
| `check-dist-fresh.yml` | Locale, SEO source, or generator changes | Rebuilds generated artifacts and fails when tracked `dist/` output is stale. |
| `build-dist.yml` | Locale or SEO source changes on main | Rebuilds and commits changed `dist/` artifacts. |
| `purge-cdn.yml` | Changes under `dist/` | Requests jsDelivr cache purges for generated bundles. |
| `notify-docs.yml` | Core-module locale changes | Dispatches a documentation regeneration event. |
| `sync.yml` | Repository dispatch or manual run | Opens reviewed synchronization pull requests from Core. |
| Cloud-owned `trigger-i18n-sync.yml` | Cloud frontend changes or manual run | Runs the i18n Cloud scanner beside the private source and opens a reviewed pull request here. |
| `release.yml` | Version tag | Validates and packages source locale archives as a GitHub release. |

Consumers decide whether they fetch CDN artifacts at runtime or bundle copied
artifacts during their own build. A push is not considered live until the
relevant workflow, cache, and consumer checks succeed.

## Testing

The closed-loop test gate compiles every Python file, runs Ruff, checks the
generated Python declaration reference, validates all source catalogs and the root
manifest, runs the regression suite, and rebuilds translation and SEO output:

```bash
npm run verify
```

Placeholder parity remains a separate report-only migration gate. See
[`STATE.md`](STATE.md) for the current baseline and release evidence.

## Scripts

Install Python 3.11 or newer and the pinned dependencies before running the
repository verification commands:

```bash
python3 -m pip install -r requirements.txt
```

```bash
# Validate everything
python scripts/validate.py --strict

# Full local closed-loop gate
npm run verify

# Same gate without npm
make verify

# Check coverage
python scripts/coverage.py

# Report placeholder-set drift without changing catalogs
python scripts/audit-placeholders.py --json

# Verify every Python declaration has current source-linked documentation
python scripts/generate-reference.py

# Build translation dist for CDN
python scripts/build-dist.py

# Build public multilingual SEO manifest
python scripts/build-seo-manifest.py

# Check SEO manifest freshness without writing
python scripts/build-seo-manifest.py --check

# Add a new language
python scripts/add-locale.py <code>

# Sync keys from flyto-core modules
python scripts/sync-from-core.py --core-path ../flyto-core --dry-run

# Sync keys from flyto-cloud UI ($t() calls)
python scripts/sync-from-cloud.py --cloud-path ../flyto-cloud --dry-run

# Regenerate and copy the offline Flyto2 Flow scope
python scripts/sync-to-projects.py --project flow
```

Both sync commands preserve scanner-omitted keys by default. The optional
`--delete-stale` flag is destructive; use it only after reviewing a dry-run and
proving the scanner covers dynamic and compatibility keys.

See the [tooling reference](docs/TOOLING.md) before running commands that write
source catalogs, generated output, sibling repositories, GitHub, or OpenAI.
The [generated Python reference](docs/generated/python-symbols.md) maps every
maintained, historical, and test declaration to its source contract.

## Environment

Most commands in this repository are local and deterministic. Validation,
coverage, dist build, locale sync, and consumer sync do not need credentials.

Create a local `.env` only when running optional assisted translation tooling:

```bash
cp .env.example .env
```

`OPENAI_API_KEY` is read only by `scripts/translate-with-openai.py`. Do not put
real API keys in tracked files.

## Contributing

Use `CONTRIBUTING.md` for review expectations and `workflows/` for task-specific
checklists. For changes that affect generated `dist/` output or consuming app
sync, include these checks before pushing:

```bash
python3 scripts/validate.py --strict
python3 scripts/build-dist.py
python3 scripts/build-seo-manifest.py
npm run verify
```

## API Endpoints

```
# Translations (scope = flow | cloud | code | landing | app | console | data | engine)
https://raw.githubusercontent.com/flytohub/flyto-i18n/main/dist/{scope}/{locale}.json

# Manifest (locale metadata + completion %)
https://raw.githubusercontent.com/flytohub/flyto-i18n/main/dist/{scope}/manifest.json

# Shared locale metadata
https://raw.githubusercontent.com/flytohub/flyto-i18n/main/dist/locale-meta.json

# Public SEO contract
https://raw.githubusercontent.com/flytohub/flyto-i18n/main/dist/seo-manifest.json

# Flags
https://raw.githubusercontent.com/flytohub/flyto-i18n/main/dist/flags/{region}.svg
```

## License

MIT
