# coding=utf-8
from common.mymako import render_mako_context, render_json
from common.log import logger

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.conf import settings

from home.school_views import locate_required
from home.models import School, Store

# 首页必须调用装饰器login_required
@locate_required
def home(request):
    '''
    @summary: 首页
    '''
    school = School.objects.get(id=request.session['school_id'])
    return render_mako_context(request, '/show/home.html', locals())

@locate_required
def show_mall(request):
    '''
    @summary: 根据学校定位，罗列店家信息
    '''
    school = School.objects.get(id=request.session['school_id'])
    return render_mako_context(request, '/show/mall.html', locals())

@locate_required
def show_store(request, store_id):
    '''
    @summary: 根据商家id，罗列商家商品信息
    '''
    school = School.objects.get(id=request.session['school_id'])
    store = Store.objects.get(id=store_id)
    goods = store.goods.all()
    total = goods.count()
    return render_mako_context(request, '/show/store.html', locals())

@locate_required
def show_good(request, store_id, good_id):
    '''
    @summary: 先定位商家，再定位商品，显示商品具体信息
    '''
    school = School.objects.get(id=request.session['school_id'])
    store = Store.objects.get(id=store_id)
    good = store.goods.get(id=good_id)
    return render_mako_context(request, '/show/good.html', locals())
    