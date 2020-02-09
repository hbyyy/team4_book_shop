FROM            python:3.7-slim

RUN             apt -y update && apt -y dist-upgrade && apt -y autoremove
RUN             apt -y install nginx

COPY            ./requirements.txt /tmp/
RUN             pip install -r /tmp/requirements.txt


COPY            . /srv/Book_shop
RUN             cp /srv/Book_shop/.config/book_shop.nginx /etc/nginx/sites-enabled/
WORKDIR         /srv/Book_shop/app