build:
	docker build -t python-load-balancer .

compose:
	docker compose up --build -d

lint:
	poetry run ruff check .

lint.format:
	poetry run ruff format .

lint.imports:
	poetry run ruff check . --select I --fix

test:
	poetry run python -m pytest -s -vv
