# coding=utf-8
from common.model2json import render_mjson, to_dict
from home.models import Good, Store


def get_good_list(request):
    '''
    @summary: 
    '''
    store_id = request.GET['store_id']
    store = Store.objects.get(id=int(store_id))
    begin = request.GET.get('begin', 0)
    num = request.GET.get('num', 8)
    goods = _get_goods(store, begin, num)
    return render_mjson([to_dict(_g) for _g in goods])
    
    
    

#===============================================================================
# 内部函数
#===============================================================================
def _get_goods(store=None,begin=0,num=8,order='-go_online_time'):
    '''
    @summary:         返回店家相关商品信息，分页返回
    @param stroe:     home.models.Store对象
    @param begin:     Good对象排序后，开始序号
    @param num:       返回 Good 对象的数量
    @param order:     使用 Good.objects.all().order_by(order),
                                                        排序条件 默认 '-go_online_time'，按照上线时间，倒序
    '''
    goods = store.goods.order_by(order) if store else []
    return goods[begin:begin+num]