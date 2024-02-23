.PHONY: install test lint-check coverage
default: help

help:
	@echo "install - install dependencies"
	@echo "test - run tests"
	@echo "lint-check - run linter check"

install:
	@poetry install

test:
	@poetry run pytest -vv

lint-check:
	@echo "running linting..."
	@echo "running flake8..."
	@poetry run flake8 .
	@echo "running mypy..."
	@poetry run mypy .
	@echo "running black..."
	@poetry run black --check .
	@echo "running isort..."
	@poetry run isort --check .
	@echo "end of linting..."

coverage:
	@poetry run pytest --cov=pymodoro pymodoro/tests/