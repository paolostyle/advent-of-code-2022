lint:
	flake8 . && mypy . && black . --check && isort . --check

format:
	black . && isort .
