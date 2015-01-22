# coding=utf-8
'''
context_processor for common(setting)

'''
from django.conf import settings


def mysetting(request):
    return {'MEDIA_URL': settings.MEDIA_URL,
            'STATIC_URL': settings.STATIC_URL,
            'RUN_MODE': settings.RUN_MODE,                              # 运行模式 
            }
