lint:
	poetry run ruff check .
lint.format:
	poetry run ruff format .
lint.imports:
	poetry run ruff check . --select I --fix
