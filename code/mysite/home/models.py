#coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
    name = models.CharField(u"学校名称", max_length=100)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = u"学校"
        verbose_name_plural = u"学校"


class Store(models.Model):
    area = models.ForeignKey(School, verbose_name=u"所属学校", related_name='stores')
    owner = models.ForeignKey(User, verbose_name=u"店主", related_name='stores')
    created_time = models.DateTimeField(u"创建时间")
    name = models.CharField(u"店名", max_length=100)
    summary = models.CharField(u"简要介绍", max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return u"%s %s" %(self.area, self.name)
    
    class Meta:
        verbose_name = u"店家"
        verbose_name_plural = u"店家"

class Good(models.Model):
    store = models.ForeignKey(Store,verbose_name=u"所属店家",related_name='goods')
    name = models.CharField(u"商品名称", max_length=100)
    options = models.TextField(u"商品选项-json串")
    prices = models.TextField(u"商品价格-json串")
    min_price = models.FloatField(u"最低价格")
    go_online_time = models.DateTimeField(u"上线日期")
        
    def __unicode__(self):
        return u"%s %s" %(self.store, self.name)
    
    class Meta:
        verbose_name = u"商品"
        verbose_name_plural = u"商品"
        
