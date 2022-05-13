.PHONY: all bandit black flake8 isort mypy pylint lint

all: lint

# Test folder excluded
bandit:
	bandit -r wordler

black:
	black wordler tests --check --verbose

flake8:
	flake8 wordler tests --max-line-length=88 --max-doc-length=79

isort:
	isort wordler tests --diff

mypy:
	mypy -m wordler -m tests

pylint:
	pylint wordler tests

lint: bandit black flake8 isort mypy pylint
