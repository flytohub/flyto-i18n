# Feature Reference

## Translation Source Catalogs

Human-edited JSON under `locales/{project}/{locale}/` is the source of truth.
The shared contract currently recognizes cloud, modules, landing, shared, app,
code, console, data, and engine projects. English defines the key baseline;
official and community locales may leave values empty to request English
fallback.

## Validation And Coverage

`validate.py` applies the tracked Draft-07 locale and repository-manifest
schemas, then checks key compatibility, injection markers, corrupted
replacement markers, and critical translation requirements. `coverage.py`
measures unique non-empty merged keys against English by locale and project.
`audit-placeholders.py` separately inventories placeholder-set drift so legacy
translation debt can be repaired without weakening schema validation. Coverage
is a completeness signal, not a linguistic-quality score.

## Deterministic Distribution Build

`build-dist.py` merges source files into nested CDN bundles for cloud, landing,
app, code, console, data, and engine plus a full aggregate bundle. Versions and
manifests are content-derived, so an unchanged source produces unchanged JSON.
`build-seo-manifest.py` separately produces the public SEO contract. The
aggregate build also synchronizes root `manifest.json` coverage from the
generated aggregate manifest.

## Source-Linked Documentation

`generate-reference.py` parses maintained tooling, historical migrations, and
tests with Python AST. It requires every class, function, nested function,
method, and test to have a docstring and freshness-checks the tracked generated
reference.

## Locale Metadata

`i18n_contract.py` centralizes launch order, names, native labels, regions,
directions, `hreflang`, Open Graph locale values, and flag filenames.
`dist/locale-meta.json` is the generated consumer contract.

## Multilingual SEO

`seo/public-surfaces.json` defines canonical origins, sitemap locations, route
patterns, required signals, keyword intent, long-tail clusters, and dated
research evidence for landing, docs, and blog. The builder expands every
shipped locale into alternate URL templates and adds `x-default`.

## Upstream Key Synchronization

Core and Cloud scanners discover translatable keys from sibling source trees.
Synchronization commands update source catalogs and should be reviewed in pull
requests; they do not grant upstream code or translation correctness. Both
scanners preserve existing keys by default. `--delete-stale` is destructive and
must be used only after reviewing a dry-run scanner-completeness report.

## Consumer Synchronization

`sync-to-projects.py` copies built bundles into supported sibling repositories,
removes stale locale files, and can run in dry-run mode. Consumers may instead
load raw GitHub or jsDelivr artifacts. Each consumer owns runtime caching,
fallback, deployment, and failure behavior.

## Assisted Translation

`translate-with-openai.py` is optional, networked, and requires
`OPENAI_API_KEY`. Generated translations are drafts requiring placeholder,
terminology, privacy, and native-language review before merge.

## Release And Cache Automation

GitHub Actions validates source, rejects stale generated output, rebuilds main,
purges CDN paths, opens reviewed upstream-sync pull requests, notifies docs for
module changes, and packages version-tag releases. Successful GitHub Actions do
not prove that every downstream cache has refreshed.
