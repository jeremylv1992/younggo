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
)


if settings.RUN_MODE=='DEVELOP':
    import os, django
    urlpatterns += patterns('',
        # ADMIN_MEDIA_PREFIX , 注意，这个url不要删除，否则开发的时候，进入admin时候，不会显示样式，也不会加载对应的js
        url(r'^static/lib/django-1.3.1/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': os.path.join(django.__path__[0], 'contrib/admin/media/'),
        }),
        # media
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )
