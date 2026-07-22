PYTHON ?= python3

.PHONY: lint docs-check docs-write test build verify

lint:
	$(PYTHON) -m compileall -q scripts tests translate_th.py
	ruff check scripts tests translate_th.py
	$(MAKE) docs-check

docs-check:
	$(PYTHON) scripts/generate-reference.py

docs-write:
	$(PYTHON) scripts/generate-reference.py --write

test:
	$(PYTHON) scripts/validate.py --strict
	$(PYTHON) scripts/coverage.py
	$(PYTHON) -m unittest discover -s tests

build:
	$(PYTHON) scripts/build-dist.py
	$(PYTHON) scripts/build-seo-manifest.py

verify: lint test build
