# flyto-i18n

Internationalization (i18n) language packs for the flyto ecosystem.

## Overview

This repository contains translation files for all flyto projects. Translations are organized by project and community-driven.

## Structure

```
flyto-i18n/
├── locales/
│   ├── cloud/                     # flyto-cloud UI translations
│   │   ├── en/
│   │   │   ├── admin.json
│   │   │   ├── dashboard.json
│   │   │   └── ...
│   │   ├── zh-TW/
│   │   ├── ja/
│   │   └── ...
│   ├── modules/                   # flyto-core module translations
│   │   ├── en/
│   │   │   ├── browser.json
│   │   │   ├── flow.json
│   │   │   └── ...
│   │   └── ...
│   ├── landing/                   # flyto-landing-page translations
│   │   ├── en/
│   │   └── ...
│   └── shared/                    # Shared translations (common, app)
│       ├── en/
│       │   ├── common.json
│       │   ├── app.json
│       │   └── ...
│       └── ...
├── dist/                          # Built files for CDN
├── schema/                        # JSON Schema validation
├── scripts/                       # Build & validation tools
└── manifest.json                  # Language pack metadata
```

## Available Languages

| Locale | Language | Status |
|--------|----------|--------|
| en | English | Official |
| zh-TW | 繁體中文 | Official |
| zh-CN | 简体中文 | Official |
| ja | 日本語 | Official |
| ko | 한국어 | Community |
| fr | Français | Community |
| es | Español | Community |
| de | Deutsch | Community |
| pt-BR | Português (Brasil) | Community |
| it | Italiano | Community |
| vi | Tiếng Việt | Community |
| th | ภาษาไทย | Community |
| id | Bahasa Indonesia | Community |
| hi | हिन्दी | Community |
| tr | Türkçe | Community |
| pl | Polski | Community |

## Usage

### CDN (jsDelivr)

```
https://cdn.jsdelivr.net/gh/flytohub/flyto-i18n@main/dist/cloud/{locale}.json
https://cdn.jsdelivr.net/gh/flytohub/flyto-i18n@main/dist/landing/{locale}.json
```

### For Frontend (flyto-cloud)

```typescript
const response = await fetch('https://cdn.flyto2.net/i18n/cloud/zh-TW.json');
const translations = await response.json();
```

### For Backend (flyto-core)

```python
from core.i18n import Translator

translator = Translator(locale='zh-TW')
label = translator.translate('modules.browser.click.label')  # "點擊元素"
```

## Translation Key Format

### Module Keys

```
modules.{category}.{module_name}.label
modules.{category}.{module_name}.description
modules.{category}.{module_name}.params.{param_name}
modules.{category}.{module_name}.params.{param_name}.options.{value}
```

### Cloud UI Keys

```
cloud.{category}.{path}.{to}.{key}
```

## Contributing

We welcome translation contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start

1. Fork this repository
2. Edit files under `locales/{project}/{your-language}/`
3. Run validation: `python scripts/validate.py --locale <your-language>`
4. Submit a Pull Request

## Scripts

| Script | Description |
|--------|-------------|
| `sync-from-core.py` | Sync keys from flyto-core modules |
| `sync-from-cloud.py` | Sync keys from flyto-cloud UI |
| `sync-locales.py` | Sync all locales with English base |
| `validate.py` | Validate translation files |
| `coverage.py` | Generate coverage report |
| `build-dist.py` | Build distribution files for CDN |
| `build-app.py` | Build files for Flutter app |
| `translate-with-openai.py` | AI-powered translation |
| `convert-tw-to-cn.py` | Convert zh-TW to zh-CN |
| `add-locale.py` | Add a new locale |

### Common Workflows

```bash
# Validate all translations
python scripts/validate.py --strict

# Validate specific project
python scripts/validate.py --project cloud

# Build dist for CDN
python scripts/build-dist.py

# Translate cloud UI to Japanese
python scripts/translate-with-openai.py --target ja --project cloud

# Sync from flyto-core
python scripts/sync-from-core.py --core-path ../flyto-core

# Add a new language
python scripts/add-locale.py ru
```

## License

MIT License - see [LICENSE](LICENSE)

## Links

- [flyto-core](https://github.com/flytohub/flyto-core) - Module core
- [flyto-cloud](https://github.com/flytohub/flyto-cloud) - Web frontend
- [Contributing Guide](CONTRIBUTING.md)
