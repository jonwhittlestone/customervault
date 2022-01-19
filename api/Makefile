.PHONY: tests

api-install:
	poetry install && exit;

api-tests:
	poetry run python -m pytest app/tests --cov-config=.coveragerc --cov=./app --maxfail=1 --tb=short
