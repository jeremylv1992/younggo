# coding=utf-8
from datetime import datetime

from django.http import HttpResponse
from common.log import logger
from common.mymako import render_json, render_mako_context
from common.model2json import to_dict, render_mjson

from cart.models import ShoppingItem
from cart.views import clear_shopping_cart
from order.models import Address, Order, OrderItem
from order.forms import AddressForm

def order_manage(request):
    '''
    @summary: 返回订单管理页面
    '''
    orders = request.user.orders.all()
    return render_mako_context(request, '/order/order_manage.html', locals())
    
def checkout(request):
    '''
    @summary: 返回确认下单页面
    '''
    items = request.user.shopping_items.all()
    return render_mako_context(request, '/order/checkout.html', locals())

def test_success(request):
    '''
    @summary: 测试订单提交成功的提示页面
    '''
    return render_mako_context(request, '/order/order_success.html', {})
    
def generate(request):
    '''
    @summary: 生成订单
    '''
    try:
        address_id = request.POST['address_id']
        addr = Address.objects.get(id=int(address_id))
        
        pay_way = request.POST['pay_way']
        items = request.user.shopping_items.all()
  
        groups = _classify_shopping_goods(items)
        for _g in groups.values():
            trans_fare = 10
            total_fare = 0
            order = Order.objects.create(customer=request.user,
                                         store=_g[0],
                                         address=addr,
                                         pay_way=int(pay_way),
                                         time=datetime.now(),
                                         trans_fare=trans_fare,
                                         total_fare=total_fare)
            for _i in _g[1]:
                order.order_items.create(good=_i.good,
                                         options=_i.options,
                                         amount=_i.amount,
                                         unit_price=_i.unit_price)
                total_fare += _i.amount*_i.unit_price
            order.total_fare = total_fare    
            order.save()
        clear_shopping_cart(request.user)
        return render_mako_context(request, '/order/order_success.html', {})
    except Exception, e:
        logger.error()
        return HttpResponse(str(e))

def _classify_shopping_goods(items):
    '''
    @summary: 对购物车的商品按照商店分组
    '''
    groups = {}
    for _i in items:
        if _i.good.store.id not in groups.keys():
            groups[_i.good.store.id] = [_i.good.store, []]
        groups[_i.good.store.id][1].append(_i)
    return groups  
                
def update_addr(request):
    '''
    @summary: 更新地址
    '''
    try:
        id = request.POST['id']
        if id == '':
            form = AddressForm(data=request.POST)        
        else:
            addr = Address.objects.get(id=int(id))
            form = AddressForm(data=request.POST, instance=addr)
        if form.is_valid():
            n_addr = form.save(commit=False)
            n_addr.user = request.user
            n_addr.save()
            return render_json({'result':True})
        else:
            return render_json({'result':False, 'message':form.errors})
    except Exception, e:
        logger.error()
        return render_json({'result':False, 'message':str(e)})

def get_all_addr(request):  
    '''
    @summary: 返回登录用户所有的送货地址
    '''
    return render_mjson([to_dict(_a) for _a in request.user.addresses.all()])