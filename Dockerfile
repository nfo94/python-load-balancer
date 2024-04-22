FROM python:3.11-slim-buster

WORKDIR /app

ADD . /app

RUN pip install poetry

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

ENV FLASK_APP=python_load_balancer/app.py

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0", "--port=5001"]
