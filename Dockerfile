FROM python:3.12.4-alpine
WORKDIR /chat_parser
RUN apk upgrade --update && apk add gcc gcompat musl-dev libffi-dev build-base unixodbc-dev unixodbc --no-cache
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY .env .
COPY settings.py .
COPY main.py .
COPY parser.session .