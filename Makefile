.PHONY: setup test lint fmt

setup:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

lint:
	ruff check src tests

fmt:
	ruff format src tests
