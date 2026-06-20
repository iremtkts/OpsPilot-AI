.PHONY: sync lint format format-check typecheck test test-cov quality pre-commit

sync:
	uv sync

lint:
	uv run ruff check .

format:
	uv run ruff format .

format-check:
	uv run ruff format --check .

typecheck:
	uv run mypy .

test:
	uv run pytest

test-cov:
	uv run pytest --cov

quality: lint format-check typecheck test

pre-commit:
	uv run pre-commit run --all-files
