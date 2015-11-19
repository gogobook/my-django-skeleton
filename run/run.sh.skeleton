#!/bin/sh

NAME=example.com
SRCDIR=example.com

GUNICORN=gunicorn
HOMEDIR=/home/django

VIRTUALENV=${HOMEDIR}/virtualenvs/${NAME}
PROJECTDIR=${HOMEDIR}/projects/${NAME}
ADDRES=127.0.0.1
PORT=8001

. ${VIRTUALENV}/bin/activate
cd ${PROJECTDIR}
gunicorn src.wsgi:application --bind ${ADDRES}:${PORT}