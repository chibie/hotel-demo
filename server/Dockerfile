FROM python:3.8-slim-buster

LABEL maintainer "Chibuotu Amadi <chibuotu@gmail.com>"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
     && apt-get install -y --no-install-recommends git \
     && python -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app
COPY . /app

RUN pip install -r ./requirements.txt
