# syntax=docker/dockerfile:1
FROM ubuntu:22.04 as base

RUN apt update

RUN apt -y install build-essential
RUN apt -y install libssl-dev
RUN apt -y install libboost-all-dev

RUN apt -y install default-jdk

RUN apt -y install python3
RUN apt -y install python3-pip

RUN pip3 install numpy

WORKDIR /app
COPY app.py app.py
CMD ["python3", "app.py"]
