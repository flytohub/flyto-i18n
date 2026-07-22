# tests/

Regression tests for locale tooling. These tests focus on script behavior that
can silently break source-to-dist or dist-to-consumer synchronization.

## Run

```bash
python3 -m unittest discover -s tests
```

The repository-level verification command also runs schema validation and
coverage:

```bash
npm run verify
```

## Test Scope

- Locale creation and metadata handling.
- Draft-07 schema and critical-copy validation.
- Placeholder extraction and audit semantics.
- Root manifest coverage synchronization.
- Consumer sync behavior.
- Guardrails for generated output freshness.
