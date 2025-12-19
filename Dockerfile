# inherit from a base image
FROM python:3.12-slim

# set working directory
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# copy rest of the local-files to working directory of container
COPY . .

# set env vars
ENV PYTHONUNBUFFERED=1

