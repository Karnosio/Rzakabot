FROM python:3.9.21-slim

WORKDIR /usr/src/app/bot

COPY requirements.txt /usr/src/app/bot

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app/bot