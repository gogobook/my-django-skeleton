#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .common import *

try:
    from .local import *
except ImportError:
    print("Can't find module settings.local! Make it from local.py.skeleton")
