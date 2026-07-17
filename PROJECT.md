# Project

`flyto-i18n` is the Flyto2 localization and multilingual SEO contract repo.

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
