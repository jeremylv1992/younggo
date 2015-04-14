# -*- coding: utf-8 -*-
from django.conf.urls import url, patterns, include
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.contrib import admin
from .views import BroadcastChatView, UserChatView, GroupChatView
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^chat/$', BroadcastChatView.as_view(), name='broadcast_chat'),
    url(r'^userchat/$', UserChatView.as_view(), name='user_chat'),
    url(r'^groupchat/$', GroupChatView.as_view(), name='group_chat'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('user_chat'))),
)

urlpatterns += patterns('chatserver.views',
	url(r'^send_message/$', 'send_message'),
)