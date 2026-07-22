# Flyto2 Internationalization Whitepaper

## Abstract

Flyto2 i18n is the shared source of truth for product translations, locale
metadata, generated distribution bundles, and multilingual SEO contracts.
It lets applications and public sites consume one reviewed language contract
without maintaining incompatible copies.

## Source And Distribution Model

Human-edited JSON under locales/ is authoritative. Stable dotted keys, English
baselines, named placeholders, and locale metadata form the source contract.
Deterministic builders publish scoped bundles, aggregate bundles, flags,
completion metadata, and SEO artifacts under dist/.

Generated output is reviewed and tracked but is never the editing source.
Consumers may load CDN bundles or package local copies for offline use. A
successful build proves deterministic transformation, not that a consuming
deployment has refreshed its cache.

## Translation Semantics

Missing localized keys may fall back to English. Fallback availability is not
translation completion. Coverage counts unique keys, validates required
locales, and audits placeholder-set parity so translated strings cannot drop
runtime substitutions silently.

## Multilingual Search Contract

The dated SEO source records canonical origins, sitemap surfaces, locale
alternates, search intent, and long-tail terms for the public site, docs, and
blog. Builders produce a shared manifest; each site remains responsible for
rendering canonical, hreflang, structured data, robots, and sitemap output.
Search-volume evidence has a collection date and must be refreshed rather than
presented as timeless fact.

## Tooling And Security

Read-only validators, coverage tools, extractors, locale creation, consumer
sync, and distribution builds are documented in [TOOLING.md](TOOLING.md).
Assisted translation is opt-in, may send selected public strings to an external
model, and always produces drafts for human review. Secrets and private product
content must not enter locale catalogs.

## Verification

Schema validation, baseline compatibility, security markers, placeholder
parity, deterministic rebuilds, generated source references, tests, and strict
Indexer checks form the gate. The [locale contract](LOCALE_CONTRACT.md),
[distribution contract](DISTRIBUTION.md), and
[SEO contract](SEO_CONTRACT.md) are the maintained technical authorities.

