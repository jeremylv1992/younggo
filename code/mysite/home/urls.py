# coding=utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('home.views',
    # 首页--your index
    (r'^$', 'home'),
)


