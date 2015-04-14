# coding=utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('passport.views',
                       (r'^login/$', 'login'),
                       (r'^logout/$', 'logout'),
                       (r'^register/$', 'register'),
                       (r'^get_username_list/$', 'get_username_list'),)
