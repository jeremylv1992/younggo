# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from home.models import Good, Store


class Address(models.Model):
    user = models.ForeignKey(User, verbose_name=u"使用者",
                             related_name='addresses')
    name = models.CharField(u"收货人姓名", max_length=128)
    tel = models.CharField(u"手机号码", max_length=128)
    second_tel = models.CharField(u"备用联系电话", max_length=128, null=True, blank=True)
    addr = models.CharField(u"详细地址", max_length=512);
    
    def __unicode__(self):
        return u"%s %s %s" %(self.name, self.tel, self.addr)
    
class Order(models.Model):
    customer = models.ForeignKey(User, verbose_name=u"顾客",
                                 related_name='orders')
    store = models.ForeignKey(Store, verbose_name=u"店家",
                              related_name='orders')
    address = models.ForeignKey(Address, verbose_name="送货地址",
                                related_name='orders')
    WAYS = ((1, u"货到付款"),)
    pay_way = models.IntegerField(u"支付方式", choices=WAYS)
    trans_fare = models.IntegerField(u"运费")
    total_fare = models.IntegerField(u"总费用")
    time = models.DateTimeField(u"下单时间")
    
    def __unicode__(self):
        return u"%s %s %s %s" %(self.customer, self.store,
                                self.time, self.total_fare)
        
class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name=u"所属订单", 
                              related_name='order_items')
    good = models.ForeignKey(Good, verbose_name=u"购买商品",
                             related_name='order_itmes')
    options = models.CharField(u"购买选项", max_length=256)
    amount = models.IntegerField(u"购买数量")
    unit_price = models.IntegerField(u"购买单价")    
    
    def __unicode__(self):
        return u"%s %s %s" %(self.good, self.option, self.amout)
            