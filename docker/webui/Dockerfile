FROM python:3.9.21-slim-bullseye

RUN apt update
RUN apt upgrade -y
RUN apt install curl -y

ENV TZ Asia/Tokyo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV LANG ja_JP.UTF-8

# Install bootstrap modules
RUN mkdir static
WORKDIR /static
RUN curl -o bootstrap.min.css https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
RUN curl -o bootstrap.bundle.min.js https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js

WORKDIR /app

COPY ./requirements.txt .
RUN pip3 install -r requirements.txt