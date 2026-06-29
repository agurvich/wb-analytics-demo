.PHONY: setup test lint fmt lock

setup:
	pip install -e ".[dev]"
	pre-commit install

test:
	pytest

lint:
	ruff check src tests

fmt:
	ruff format src tests

# Re-resolve the pinned environment after changing dependencies.
lock:
	uv pip compile pyproject.toml --extra dev --universal --python-version 3.11 \
		--custom-compile-command "make lock" -o requirements-lock.txt
