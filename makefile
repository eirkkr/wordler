.PHONY: all bandit black flake8 isort mypy pylint lint

all: lint

# Test folder excluded
bandit:
	bandit -r finance

black:
	black finance tests --check --verbose

flake8:
	flake8 finance tests

isort:
	isort finance tests --diff

mypy:
	mypy -m finance -m tests

pylint:
	pylint finance tests

lint: bandit black flake8 isort mypy pylint
