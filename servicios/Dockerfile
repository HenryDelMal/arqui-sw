FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir psycopg2-binary

CMD tail -f /dev/null