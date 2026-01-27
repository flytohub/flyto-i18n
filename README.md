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

## Translation Key Format

### Module Keys

```
modules.{category}.{module_name}.label
modules.{category}.{module_name}.description
modules.{category}.{module_name}.params.{param_name}
modules.{category}.{module_name}.params.{param_name}.description
modules.{category}.{module_name}.params.{param_name}.options.{value}
modules.{category}.{module_name}.output.{field}.description
```

### Examples

```json
{
  "modules.flow.trigger.label": "Trigger",
  "modules.flow.trigger.description": "Start workflow execution",
  "modules.flow.trigger.params.trigger_type": "Trigger Type",
  "modules.flow.trigger.params.trigger_type.options.manual": "Manual",
  "modules.flow.trigger.params.trigger_type.options.webhook": "Webhook",
  "modules.flow.trigger.params.trigger_type.options.schedule": "Schedule"
}
```

### How It Works

flyto-core modules use a simple format for `params_schema`:

```python
@register_module(
    module_id='flow.trigger',
    params_schema={
        # Array = dropdown options (auto-generates i18n keys)
        'trigger_type': ['manual', 'webhook', 'schedule'],

        # Other types
        'timeout': 30,        # number input
        'enabled': True,      # toggle switch
        'name': '',           # text input
    }
)
```

The sync script automatically generates i18n keys:
- `modules.flow.trigger.params.trigger_type` → "Trigger Type"
- `modules.flow.trigger.params.trigger_type.options.manual` → "Manual"
- `modules.flow.trigger.params.trigger_type.options.webhook` → "Webhook"

## Contributing

We welcome translation contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Start

1. Fork this repository
2. Create/edit files in `locales/<your-language>/`
3. Run validation: `python scripts/validate.py --locale <your-language>`
4. Submit a Pull Request

## Scripts

| Script | Description |
|--------|-------------|
| `sync-from-core.py` | Sync keys from flyto-core |
| `sync-from-cloud.py` | Sync keys from flyto-cloud UI |
| `validate.py` | Validate translation files |
| `coverage.py` | Generate coverage report |
| `build-dist.py` | Build distribution files |

### Syncing from flyto-core

```bash
# Preview changes
python scripts/sync-from-core.py --dry-run --no-delete

# Apply changes (preserve cloud UI keys)
python scripts/sync-from-core.py --no-delete

# Full sync (will delete keys not in core)
python scripts/sync-from-core.py
```

Options:
- `--core-path PATH` - Path to flyto-core (default: `../flyto-core`)
- `--dry-run` - Show changes without writing
- `--no-delete` - Preserve keys not found in core (recommended)

## License

MIT License - see [LICENSE](LICENSE)

## Links

- [flyto-core](https://github.com/flytohub/flyto-core) - Module core
- [flyto-cloud](https://github.com/flytohub/flyto-cloud) - Web frontend
- [Contributing Guide](CONTRIBUTING.md)
