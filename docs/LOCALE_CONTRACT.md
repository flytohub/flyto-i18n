# Locale Source Contract

## Directory Shape

```text
locales/{project}/{locale}/{catalog}.json
```

Each catalog is a JSON object with metadata and a `translations` object whose
keys are stable dotted identifiers. English is the baseline. Files are split by
ownership area so one translation change does not require editing a monolithic
catalog.

Recognized build projects are `cloud`, `modules`, `landing`, `shared`, `app`,
`code`, `console`, `data`, and `engine`. Additional source directories such as
`admin` or `paperclip` are not included by the current shared
`PROJECT_DIRS`/`SCOPES` build contract and must not be described as current CDN
sources until a generator mapping and tests are added.

## Key And Value Rules

- Keys remain dot-separated and stable after publication.
- Variables use named braces such as `{name}`; translated values preserve the
  same placeholder set. `audit-placeholders.py` measures this semantic rule;
  it is not yet a repository-wide blocking gate because the recorded legacy
  baseline contains 577 mismatches.
- Empty community-locale values mean that the consumer should use English.
- Catalog shape is enforced by `schema/locale.schema.json`: required metadata,
  locale/version formats, string values up to 800 characters, legal dotted or
  module-option keys, and no unknown top-level fields.
- The product name is Flyto2. Public contact addresses use `@flyto2.com`.
- HTML, scripts, secrets, customer data, and working credentials do not belong
  in translation values.
- Parent/child key collisions are preserved in generated bundles using `_self`;
  consumers that flatten bundles must restore `_self` to the parent key.

## Locale Metadata API

`scripts/i18n_contract.py` exposes:

| Symbol | Contract |
| --- | --- |
| `PROJECT_DIRS` | Source projects included in full aggregate builds and common tools. |
| `LOCALE_PRIORITY` | Stable ordering for shipped locales. |
| `LANGUAGE_META` | Display name, native name, region, hreflang, Open Graph locale, flag, and direction metadata. |
| `REGION_MAP` | Browser-locale-to-region compatibility map. |
| `language_meta(locale)` | Returns a complete known or derived metadata record. |
| `locale_sort_key(locale)` | Orders known launch locales before unknown codes. |
| `build_locale_meta(locales)` | Builds the public locale metadata document. |

## Change Workflow

1. Edit the owning `locales/**` source file.
2. Run `python3 scripts/sync-locales.py --dry-run` when English keys changed.
3. Run `python3 scripts/validate.py --strict` and inspect coverage.
4. Run `python3 scripts/audit-placeholders.py --project <scope> --locale <locale>`
   when values or placeholders changed.
5. Run `python3 scripts/build-dist.py`.
6. Run `python3 scripts/build-seo-manifest.py --check` when SEO or locale
   metadata changed.
7. Review source and generated diffs together before pushing.
