.PHONY: tests

install:
	poetry install && exit;

tests:
	python -m pytest app/tests --cov-config=.coveragerc --cov=./app --maxfail=1 --tb=short
