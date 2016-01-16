#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
from fabric.api import *

env.user = 'user'
env.project = 'example'

env.hosts = ['dev-server']
env.password = 'password'

env.pg_user = 'user_dev'
env.pg_password = '123123123'
env.pg_database = 'example'


def get_rand_str(length=16):
    return ''.join(
        [random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(length)])


@task
def deploy(user, pas):
    pass
