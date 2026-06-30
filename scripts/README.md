# scripts/

Operational tooling for validation, coverage, locale creation, source syncing,
distribution builds, and consumer sync.

## Main Commands

```bash
python3 scripts/validate.py --strict
python3 scripts/coverage.py
python3 scripts/build-dist.py
python3 scripts/sync-locales.py --project code
python3 scripts/sync-to-projects.py --project code
```

## Editing Rules

- Keep scripts deterministic unless a command explicitly documents network use.
- Do not require secrets for validation, coverage, build, or sync commands.
- `translate-with-openai.py` is optional assisted translation tooling and is
  the only script that reads `OPENAI_API_KEY`.
- Scripts that change locale source files must leave the repository in a state
  where `python3 scripts/validate.py --strict` and `python3 scripts/build-dist.py`
  pass.

## Output Boundaries

`build-dist.py` writes CDN-ready artifacts into `dist/`. `sync-to-projects.py`
copies built artifacts into consuming repositories such as `flyto-code`.
