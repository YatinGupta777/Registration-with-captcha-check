from django.conf.urls import url
from django.urls import path
from . import views as reg_views

urlpatterns = [
    path("", reg_views.signup, name = "signup"),
    path("success/", reg_views.success, name = "success"),
    url(r'^ajax/registration_attempt/$', reg_views.registration_attempt, name='registration_attempt'),
]# -*- coding: utf-8 -*-

