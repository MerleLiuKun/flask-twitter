.PHONY: clean lint test

help:
	@echo "  clean       remove unwanted stuff"
	@echo "  lint        check style with black"
	@echo "  test        run tests"

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .pytest_cache
	rm -f .coverage
	rm -fr htmlcov/

cov-term: clean-pyc
	pytest -s --cov=flask_twitter --cov-report term

cov-html: clean-pyc
	pytest -s --cov=flask_twitter --cov-report html

lint:
	black .

lint-check:
	black --check .

test:
	pytest -s
