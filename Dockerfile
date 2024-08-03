FROM python:3.11-slim

ENV POETRY_VERSION=1.8
RUN pip install poetry==${POETRY_VERSION}

WORKDIR /app
COPY pyproject.toml poetry.lock /app/
RUN poetry install --only main --no-root --no-directory
COPY . /app
RUN poetry install --only main

CMD ["poetry", "run", "python", "main.py" ]