#coding=utf-8
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # django后台数据库管理
    url(r'^admin/', include(admin.site.urls)),
    # 登录注册模块
    url(r'^passport/', include('passport.urls')),
    # 在home_application(根应用)里开始开发你的应用的主要功能
    # (此处home_application可以改成你想要的名字，但千万不能和工程名重名，否则会引起django1.3的一些问题)
    url(r'^', include('home.urls')),
    url(r'^cart/', include('cart.urls')),
    url(r'^order/', include('order.urls')),
)

if settings.WEBSOCKET_SWITCH == 'ON':
    urlpatterns += patterns('',
        # websocket-based biliteral communication
        url(r'^chat/', include('chatserver.urls')),
    )

if settings.RUN_MODE=='DEVELOP':
    import os, django
    urlpatterns += patterns('',
        # media
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
