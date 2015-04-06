# coding=utf-8
import json
from datetime import datetime, date

from django.db import models
from django.http import HttpResponse

class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj, models.Model):
            return obj.__unicode__()
        elif isinstance(obj, models.Manager):
            return 'models.Manager'
        else:
            return json.JSONEncoder.default(self, obj)
        
def to_dict(ins):
    '''
    @summary: 将对象转化为字典
    '''
    return dict((str(f), getattr(ins, str(f)))
                for f in ins._meta.get_all_field_names())
                
def render_mjson(dictionary={}):
    '''
    @summary: dictionary也可以是string, list数据
    @note: 在打包json时，会对特殊数据类型进行处理，
                            返回结果是个dict, 请注意默认数据格式:
            {'result': '', 'data':''}
    '''
    if type(dictionary) is not dict:
        # 如果参数不是dict,则组合成dict
        dictionary = {'result': True,
                      'data': dictionary,}
    return HttpResponse(json.dumps(dictionary, cls=CJsonEncoder)) 


    