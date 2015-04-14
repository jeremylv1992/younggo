#coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from home.models import Good

class ShoppingItem(models.Model):
    custom = models.ForeignKey(User, verbose_name=u"顾客", 
                               related_name='shopping_items')
    good = models.ForeignKey(Good, verbose_name=u"购买商品",
                             related_name='shopping_items')
    options = models.CharField(u"购买选项", max_length=256)
    amount = models.IntegerField(u"购买数量")
    unit_price = models.IntegerField(u"购买单价")
    
    def __unicode__(self):
        return u"%s %s %s %s" %(self.custom, self.good, 
                                self.option, self.amount)
        