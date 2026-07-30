# AI Space Dependency-Contract i18n

Flyto2 AI Space now has canonical operator copy for the per-capability device
dependency contract in English, Traditional Chinese, and Simplified Chinese.
The 44-key namespace covers automatic/custom selection, nine independent
runtime axes, derived impact summaries, and deterministic failure outcomes.

The wording is provider-, device-, and language-neutral. It does not treat a
camera as permanently weak or a robot as permanently critical. Automatic mode
stores no fixed level; custom mode exposes independent policy fields. The five
visible impact bands are explanatory UI summaries only.

Generated Cloud and aggregate distributions contain the reviewed source values,
and Flyto Cloud's tracked bundled baselines are synchronized from those
artifacts.

Verification:

- `python3 scripts/validate.py --strict`
- `python3 scripts/build-dist.py`
- `python3 -m pytest -q tests/test_ai_space_dependency_contract.py`
- Flyto Cloud `python3 scripts/check-i18n.py`
