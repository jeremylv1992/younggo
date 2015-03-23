# coding=utf-8
from common.mymako import render_mako_context, render_json
from common.log import logger

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings

# 首页必须调用装饰器login_required
def home(request):
    return render_mako_context(request, '/show/home.html', {})


