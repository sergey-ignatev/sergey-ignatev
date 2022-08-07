FROM python:3.9.5-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache zlib-dev libxml2-dev libxslt-dev jpeg-dev gettext rsync libffi-dev nginx postgresql-dev && \
    apk --update add --no-cache build-base unixodbc-dev && \
    pip3.9 install --upgrade pipenv pip

WORKDIR /app

ADD ["Pipfile", "Pipfile.lock", "/app/"]

RUN pipenv install --system --deploy

COPY . .