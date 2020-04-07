from django.conf.urls import url
from django.urls import path
from . import views as reg_views

urlpatterns = [
    path("", reg_views.signup, name = "signup"),
    path("success/", reg_views.success, name = "success"),
    url(r'^ajax/registration_attempt/$', reg_views.signup, name='signup'),
]# -*- coding: utf-8 -*-

