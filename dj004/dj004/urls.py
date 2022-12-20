"""dj004 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
# from app.views import StudentView, StudentDetailView
from app.views import StudentView
from rest_framework import routers
from django.conf.urls import url


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('dj004/', include("app.urls")),
#     # path('sm/', StudentView.as_view()),
#     # re_path('sm/(?P<pk>\d+)/', StudentDetailView.as_view()),
#     # # 终极版1
#     # path('sm/', StudentView.as_view({'get':'list', 'post':'create'})),
#     # re_path('sm/(?P<pk>\d+)/', StudentDetailView.as_view({'get':'getlist', 'put':'putlist', 'delete':'deletelist'})),
#
#     # 终极版2，继承viewsets.ViewSetMiMin,路由分发机制，对应视图融合
#     # viewSetMixin里面重写了view,用户访问url,匹配成功，形成自身view函数，
#     # 执行for循环，遍历入参字典，判断处理方法，通过入参得到对应的方法，然后
#     # 在视图对象中找对应方法，找到对应方法后，setattr,更新后，执行原来dispatch
#     # path('sm/', StudentView.as_view({'get': 'list', 'post': 'create'})),
#     # re_path('sm/(?P<pk>\d+)/', StudentView.as_view(
#     #     {'get': 'listget', 'put': 'listupdate', 'delete': 'listdelete'})),
#
# ]


router = routers.DefaultRouter()
router.register('student', StudentView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj004/', include("app.urls")),
    url('st/', include(router.urls)),
    # path('sm/', StudentView.as_view()),
    # re_path('sm/(?P<pk>\d+)/', StudentDetailView.as_view()),
    # # 终极版1
    # path('sm/', StudentView.as_view({'get':'list', 'post':'create'})),
    # re_path('sm/(?P<pk>\d+)/', StudentDetailView.as_view({'get':'getlist', 'put':'putlist', 'delete':'deletelist'})),

    # 终极版2，继承viewsets.ViewSetMiMin,路由分发机制，对应视图融合
    # viewSetMixin里面重写了view,用户访问url,匹配成功，形成自身view函数，
    # 执行for循环，遍历入参字典，判断处理方法，通过入参得到对应的方法，然后
    # 在视图对象中找对应方法，找到对应方法后，setattr,更新后，执行原来dispatch
    # path('sm/', StudentView.as_view({'get': 'list', 'post': 'create'})),
    # re_path('sm/(?P<pk>\d+)/', StudentView.as_view(
    #     {'get': 'listget', 'put': 'listupdate', 'delete': 'listdelete'})),

]