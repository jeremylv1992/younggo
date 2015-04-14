# coding=utf-8
import json

from common.mymako import render_json, render_mako_context
from common.log import logger
from cart.models import ShoppingItem
from home.models import Good


def shopping_cart(request):
    '''
    @summary: 购物车页面
    '''
    items = request.user.shopping_items.all()
    return render_mako_context(request, '/cart/shopping_cart.html', locals())

def clear_shopping_cart(user):
    '''
    @summary: 清空用户购物车
    '''
    for _i in user.shopping_items.all():
        _i.delete()
    
def add_record(request):
    '''
    @summary: 往用户的购物车添加商品，即往cart.models.Record添加一条记录
    '''
    try:
        params = json.loads(request.POST['params'])
        # 物品类别选择，提供可读性强的显示方式
        display_options = '; '.join([':'.join(opt) for opt in params['options']])
        # 根据good_id 找到物品实例
        good = Good.objects.get(id=params['good_id'])
        ShoppingItem.objects.create(custom=request.user,
                                    good=good,
                                    options=display_options,
                                    amount=params['amount'],
                                    unit_price=params['unit_price'])
    except Exception, e:
        logger.error()
        return render_json({'result':False, 'message':str(e)})
    return render_json({'result':True})

def remove_record(request):
    '''
    @summary: 从购物车移除商品
    '''
    try:
        item_id = request.POST['item_id']
        ShoppingItem.objects.get(id=item_id).delete()
    except Exception, e:
        logger.error()
        return render_json({'result':False, 'message':str(e)})
    return render_json({'result':True})

def update_amount(request):
    '''
    @summary: 更新购物车的商品数量
    '''
    try:
        item_id = int(request.POST['item_id'])
        amount = int(request.POST['amount'])
        if amount < 1:
            raise ValueError(u"非法的数量值")
        item = ShoppingItem.objects.get(id=item_id)
        item.amount = amount
        item.save()
    except Exception, e:
        logger.error()
        return render_json({'result':False, 'message':str(e)})
    return render_json({'result':True})