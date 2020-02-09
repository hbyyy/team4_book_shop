FROM            python:3.7-slim

RUN             apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN             apt -y install nginx

COPY            ./requirements.txt /tmp/
RUN             pip install -r /tmp/requirements.txt


COPY            . /srv/Book_shop
WORKDIR         /srv/Book_shop/app