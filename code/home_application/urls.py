# coding=utf-8

# import from apps here


# import from lib
from django.conf.urls.defaults import patterns, include

urlpatterns = patterns('home_application.views',
    # 首页--your index
    (r'^$', 'home'),

)
