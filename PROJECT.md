# Project

`flyto-i18n` has one public role: "Fix a translation once and share it across
every Flyto2 product, docs, and website surface."

The problem it solves is that the same product copy drifts across many Flyto2
repositories and locales. This repository owns the reviewed source catalogs
and generated distribution contracts; consuming products own their runtime
loading, fallback, and deployment behavior.

Owned surfaces:

- Runtime translation bundles for Flyto2 Cloud, Code, Console, Data, Engine,
  App, Landing, shared strings, and Flyto2 Core modules.
- Shared locale metadata for language pickers, flags, regions, `hreflang`,
  `og_locale`, and text direction.
- Public SEO contract for `flyto2.com`, `docs.flyto2.com`, and
  `blog.flyto2.com`.

Users:

- Product engineers consuming generated locale bundles.
- Public-site maintainers generating canonical URLs, alternate language links,
  sitemaps, and localized metadata.
- Translators and contributors fixing product copy.
- SEO/content maintainers tracking long-tail keyword intent by locale.

Non-goals:

- This repo does not host public websites.
- This repo does not store API keys, SMTP credentials, or translator accounts.
- This repo does not replace the source Markdown/MDX content in docs or blog.

Product lines:

- cloud_apps_automation
- security
- data
- zero_person_agent
- big_data_intelligence

Status: internal tooling with public CDN artifacts

Core dependency: localization and SEO contract tooling

Health target: B
