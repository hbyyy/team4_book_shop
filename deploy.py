#!/usr/bin/env python

import os
import subprocess
from pathlib import Path

from app.config.settings import ROOT_DIR

HOME = str(Path.home())
#
HOST = '13.125.153.207'
USER = 'ubuntu'
TARGET = f'{USER}@{HOST}'
SECRET_FILE_PATH = os.path.join(ROOT_DIR, 'secrets.json')
IDENTITY_KEY = os.path.join(HOME, '.ssh', 'ec2study.pem')

IMAGE_NAME = 'lloasd33/bookmarket'
NGINX_IMAGE_NAME = 'lloasd33/bookmarket-nginx'


def run(cmd):
    subprocess.run(cmd, shell=True)


def ssh_run(cmd):
    run(f'ssh -i {IDENTITY_KEY} {TARGET} -C {cmd}')


# 1. requirements update
def requirements_update():
    run('poetry export -f requirements.txt > requirements.txt')


def secrets_copy():
    run(f'scp -i {IDENTITY_KEY} {SECRET_FILE_PATH} {TARGET}:/home/ubuntu ')
    run(f'scp -i {IDENTITY_KEY} docker-compose.yml {TARGET}:/home/ubuntu ')


# 2. server_update & docker install
def server_update():
    ssh_run('sudo apt -y update && sudo apt -y dist-upgrade && sudo apt -y autoremove')
    # ssh_run('sudo apt install docker.io')


# 3.docker build &push
def docker_build():
    run(f'docker build -t {IMAGE_NAME} -f Dockerfile . ')
    run(f'docker build -t {NGINX_IMAGE_NAME} -f Dockerfile-nginx . ')
    run(f'docker push {IMAGE_NAME}')
    run(f'docker push {NGINX_IMAGE_NAME}')


# 4.server docker pull

def docker_pull():
    ssh_run(f'docker-compose -f docker-compose.yml pull')


def docker_run():
    ssh_run('docker-compose -f docker-compose.yml stop')
    # ssh_run('sudo docker rm book_shop')
    ssh_run(f'docker-compose -f docker-compose.yml up')


# def collect_static():
#     print('===========================collectstatic======================')
#     ssh_run('sudo docker exec book_shop python manage.py collectstatic --noinput')


# def runserver():
#     ssh_run(f'sudo docker exec -d book_shop supervisord -c ../.config/supervisor.conf -n')


if __name__ == '__main__':
    requirements_update()
    secrets_copy()
    server_update()
    docker_build()
    docker_pull()
    docker_run()
