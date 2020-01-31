FROM python:3.8.1-slim-buster

ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ./ /app

RUN pip install -r /app/reqs.txt
