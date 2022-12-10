lint:
	black . --check && isort . --check && flake8 . && mypy .

format:
	black . && isort .
