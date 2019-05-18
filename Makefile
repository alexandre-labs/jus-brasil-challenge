.PHONY: clean-build clean-pyc clean-test clean flake8 lint coverage

YELLOW=\033[1;33m
RED=\033[0;31m
GREEN=\033[0;32m
NC=\033[0m

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name 'jus_brasil-*.dist-info' -exec rm -fr {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

clean: clean-build clean-pyc clean-test

install: clean
	poetry install -vvv

update-deps: clean
	poetry update -vvv
	poetry install -vvv

flake8:
	@echo "${YELLOW}Checking flake8...${NC}\n"
	@if ! poetry run flake8 eight_ball; then \
	echo "${RED}\nflake8 failed${NC}"; \
	    exit_code=2; \
	else \
	    echo "\n${GREEN}flake8 OK${NC}"; \
	fi

mypy:
	mypy --ignore-missing-imports jus_brasil

lint: flake8 mypy

coverage: lint
	poetry run py.test --cov=jus_brasil --cov-fail-under=90 --cov-report=html

test: lint
	@if poetry run pytest tests/unit tests/integration ; then \
	echo "\n${GREEN}SUCCESS: All tests passed.${NC}\n" ; \
	else \
	echo "\n${RED}FAILURE: One or more tests have failed.${NC}\n" && exit 1 ; \
	fi