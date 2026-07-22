# schema/

JSON schema definitions for repository metadata and locale file validation.

## Files

- `locale.schema.json`: validates every recognized
  `locales/{scope}/{locale}/*.json` source file. Empty strings are valid English
  fallback markers; values are capped at 800 characters.
- `manifest.schema.json`: validates the repository-level `manifest.json`.

## Contract

`scripts/validate.py` loads both Draft-07 schemas and fails strict validation on
shape violations. Direct compatibility files outside the recognized project
contract, such as `locales/landing/app.json` and `locales/paperclip/**`, are not
covered until they receive an explicit source/generator mapping.

Schema changes affect validation for all recognized product scopes. When
changing a schema, run:

```bash
python3 scripts/validate.py --strict
npm run verify
```
