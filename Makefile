PYTHON ?= python3

.PHONY: lint test build verify

lint:
	$(PYTHON) -m compileall -q scripts

test:
	$(PYTHON) scripts/validate.py --strict
	$(PYTHON) scripts/coverage.py
	$(PYTHON) -m unittest discover -s tests

build:
	$(PYTHON) scripts/build-dist.py
	$(PYTHON) scripts/build-seo-manifest.py

verify: lint test build
