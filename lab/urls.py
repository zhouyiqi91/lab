from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from lab.views import *

urlpatterns = [
    url(r'^$',display),
    url(r'^(?P<project_uid>[0-9]+)/$', sample_lists, name='sample_lists'),
    ]