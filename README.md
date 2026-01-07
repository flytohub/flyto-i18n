# flyto-i18n

Internationalization (i18n) language packs for [flyto-core](https://github.com/flytohub/flyto-core).

## Overview

This repository contains translation files for all flyto-core modules. Translations are community-driven and follow a structured contribution process.

## Structure

```
flyto-i18n/
├── locales/
│   ├── en/                    # English (base, auto-generated)
│   ├── zh-TW/                 # Traditional Chinese
│   ├── zh-CN/                 # Simplified Chinese
│   ├── ja/                    # Japanese
│   └── ...
├── schema/                    # JSON Schema validation
├── scripts/                   # Build & validation tools
└── manifest.json              # Language pack metadata
```

## Available Languages

| Locale | Language | Coverage | Status |
|--------|----------|----------|--------|
| en | English | 100% | Official |
| zh-TW | 繁體中文 | - | Coming Soon |
| zh-CN | 简体中文 | - | Coming Soon |
| ja | 日本語 | - | Coming Soon |

## Usage

### For Frontend (flyto-cloud)

```typescript
// Download language pack
const response = await fetch('https://cdn.flyto2.net/i18n/zh-TW/latest.json');
const translations = await response.json();

// Or use the i18n service
import { useI18n } from '@flyto/i18n';

const i18n = useI18n();
await i18n.setLocale('zh-TW');
console.log(i18n.t('modules.browser.click.label')); // "點擊元素"
```

### For Backend (flyto-core)

```python
from core.i18n import Translator

translator = Translator(locale='zh-TW')
label = translator.translate('modules.browser.click.label')  # "點擊元素"
```

## Contributing

We welcome translation contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start

1. Fork this repository
2. Create/edit files in `locales/<your-language>/`
3. Run validation: `python scripts/validate.py --locale <your-language>`
4. Submit a Pull Request

### Translation Key Format

```
modules.{category}.{module_name}.{section}.{field}

Examples:
- modules.browser.click.label
- modules.browser.click.description
- modules.browser.click.params.selector.label
- modules.browser.click.output.status.description
```

## Scripts

| Script | Description |
|--------|-------------|
| `scripts/sync-from-core.py` | Sync keys from flyto-core (maintainers only) |
| `scripts/validate.py` | Validate translation files |
| `scripts/coverage.py` | Generate coverage report |
| `scripts/build.py` | Build distribution files |

## License

MIT License - see [LICENSE](LICENSE)

## Links

- [flyto-core](https://github.com/flytohub/flyto-core) - Module core
- [flyto-cloud](https://github.com/flytohub/flyto-cloud) - Web frontend
- [Contributing Guide](CONTRIBUTING.md)
