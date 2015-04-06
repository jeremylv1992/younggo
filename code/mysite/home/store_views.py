# coding=utf-8
from common.model2json import render_mjson, to_dict

from home.school_views import locate_required
from home.models import Store, School

@locate_required
def get_store_list(request):
    '''
    @summary: 根据返回商店列表
    '''
    school = School.objects.get(id=request.session['school_id'])
    begin = request.GET.get('begin', 0)
    num = request.GET.get('num', 8)
    stores = _get_stores(school, begin, num)
    return render_mjson([to_dict(_s) for _s in stores])



#===============================================================================
# 内部函数
#===============================================================================
def _get_stores(school=None,begin=0,num=8,order='-created_time'):
    '''
    @summary:         返回学校相关的店铺信息，分页返回
    @param school:    home.models.School 对象，可查询到关联的Store对象
    @param begin:     Store对象排序后，开始序号
    @param num:       返回Store 对象的数量
    @param order:     使用 Store.objects.all().order_by(order),
                                                        排序条件 默认 '-create_time'，按照创建时间，倒序
    '''
    stores = school.stores.order_by(order) if school else \
                Store.objects.all().order_by(order)
    return stores[begin:begin+num]
        