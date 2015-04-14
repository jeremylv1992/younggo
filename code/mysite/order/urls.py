# coding=utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('order.views',
    url(r'^$', 'order_manage'),
    url(r'^checkout/$', 'checkout'),
    url(r'^generate/$', 'generate'),
    url(r'^test_success/$', 'test_success'),
    
    url(r'^addr/update/$', 'update_addr'),
    url(r'^addr/get_all/$', 'get_all_addr'),
)