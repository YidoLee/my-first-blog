"""
Author: DOYEONG LEE
Date: 2017-00-00
Brief: 
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]