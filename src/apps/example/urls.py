#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import home


urlpatterns = (
    url(r'^$', home, name='index'),
)