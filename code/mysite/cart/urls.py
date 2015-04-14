# coding=utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('cart.views',
    url(r'^$', 'shopping_cart'),
    url(r'^add_record/$', 'add_record'), 
    url(r'^remove_record/$', 'remove_record'),     
    url(r'^update_amount/$', 'update_amount'),             
)