FROM python:3.7.5-buster

ENV PYTHONPATH /home/user/code/src:$PYTHONPATH

ADD requirements.txt /tmp/requirements.txt

WORKDIR /tmp

RUN set -eux; \
    useradd -ms /bin/bash user; \
    pip install -r /tmp/requirements.txt

WORKDIR /home/user/code

