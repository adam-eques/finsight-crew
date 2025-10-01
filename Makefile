.PHONY: install lint test fmt run clean

install:
	pip install -e . && pip install ruff pytest

lint:
	ruff check src tests

fmt:
	ruff format src tests

test:
	pytest -q

run:
	finsight research AAPL -q "Is the balance sheet healthy?"

clean:
	rm -rf build dist *.egg-info .pytest_cache .ruff_cache
