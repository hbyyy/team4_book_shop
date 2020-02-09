#!/usr/bin/env python

import os
import subprocess
from pathlib import Path

HOME = str(Path.home())
HOST = '15.164.98.120'
USER = 'ubuntu'
TARGET = f'{USER}@{HOST}'
SECRET_FILE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'secrets.json')
IDENTITY_KEY = os.path.join(HOME, '.ssh', 'wps-bookshop.pem')


def run(cmd):
    subprocess.run(cmd, shell=True)


def ssh_run(cmd):
    run(f'ssh -i {IDENTITY_KEY} {TARGET} -C {cmd}')


# 1. requirements update
def requirements_update():
    run('pip freeze > requirements.txt')


# 2. server_update & docker install
def server_update():
    ssh_run('sudo apt -y update && sudo apt -y dist-upgrade && sudo apt -y autoremove')
    ssh_run('sudo apt install docker.io')


# 3.docker build &push
def docker_build():
    run('docker build -t lloasd33/book_shop -f Dockerfile . ')
    run('docker push lloasd33/book_shop')


# 4.server docker pull

def docker_pull():
    ssh_run('sudo docker pull lloasd33/book_shop')


def docker_run():
    ssh_run('sudo docker stop book_shop')
    # ssh_run('sudo docker rm book_shop')
    ssh_run('sudo docker run --rm -it -d -p 80:80 --name book_shop lloasd33/book_shop /bin/bash')


def secrets_copy():
    run(f'scp -i {IDENTITY_KEY} {SECRET_FILE_PATH} {TARGET}:/tmp ')
    ssh_run(f'sudo docker cp /tmp/secrets.json book_shop:/srv/Book_shop')


def runserver():
    ssh_run(f'sudo docker exec -d book_shop python manage.py runserver 0:80')


if __name__ == '__main__':
    requirements_update()
    server_update()
    docker_build()
    docker_pull()
    docker_run()
    secrets_copy()
    runserver()
