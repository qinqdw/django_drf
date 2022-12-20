#! /usr/bin/python3
# -*- coding: utf-8 -*-
# ****************************************************
# Time    :   2022-12-20 , 0020 14:42
# Author  :   秦大伟
# Email   :   2426645196@qq.com
# File    :   urls.py
# ****************************************************

from app.views import StudentView
from rest_framework import routers
from django.urls import path, re_path

urlpatterns = [
    path('sm/', StudentView.as_view({'get': 'list', 'post': 'create'})),
    re_path('sm/(?P<pk>\d+)/', StudentView.as_view(
        {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

]

