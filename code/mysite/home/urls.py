# coding=utf-8
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('home.views',
    # 首页--your index
    url(r'^$', 'home', name='home'),
    url(r'^show/$', 'show_mall'),
    url(r'^show/(?P<store_id>\d+)/$', 'show_store'),
    url(r'^show/(?P<store_id>\d+)/(?P<good_id>\d+)/$', 'show_good'),
    url(r'^chat/', 'test_chat_page'),
)

urlpatterns += patterns('home.store_views',
     url(r'^store/get_store_list/$', 'get_store_list'),
)

urlpatterns += patterns('home.good_views',
    url(r'^good/get_good_list/$', 'get_good_list'),                    
)

urlpatterns += patterns('home.school_views',
    url(r'^school/locate/$', 'locate_school'),
    url(r'^school/get_school_list/$', 'get_school_list'),
)
