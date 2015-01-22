# coding=utf-8
from common.mymako import render_mako_context, render_json
from common.log import logger
from django.http import HttpResponse



# 首页必须调用装饰器login_required，注意：一定要import common.decorators里的login_required
def home(request):
    return render_mako_context(request, '/base.html', {})

