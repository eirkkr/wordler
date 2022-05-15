.PHONY: all bandit black flake8 isort mypy pylint lint

all: lint

# Test folder excluded
bandit:
	bandit -r wordler

black:
	black wordler --check --verbose

flake8:
	flake8 wordler --max-line-length=88 --max-doc-length=79

isort:
	isort wordler --diff

mypy:
	mypy -m wordler

pylint:
	pylint wordler

lint: bandit black flake8 isort mypy pylint
