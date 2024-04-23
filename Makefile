# To build the image
build:
	docker build -t python-load-balancer .

# To compose all containers for this app
compose:
	docker compose up --build -d

# Local development with Poetry
lint:
	poetry run ruff check .

lint.format:
	poetry run ruff format .

lint.imports:
	poetry run ruff check . --select I --fix

test:
	poetry run python -m pytest
