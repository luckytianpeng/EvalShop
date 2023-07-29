# syntax=docker/dockerfile:1

FROM python:3.10.6-slim-buster

RUN apt -y update

RUN apt -y install git
RUN pip install GitPython

# Ref:  https://pypi.org/project/virtualenv-api/
# RUN apt -y install python3-virtualenv
# RUN pip install virtualenv-api

WORKDIR /app

# Notice: tricky!
# Linux command:
#   cp -r /home/ptian/downloads/github.com/bastikr/ ./
#   cp -r /home/ptian/downloads/github.com/CoderEval/ ./
#
COPY /test_entry_points/ ./test_entry_points/
COPY /github/ ./github/
COPY app.py app.py

CMD ["python3", "app.py"]
