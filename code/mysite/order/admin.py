# coding=utf-8
from django.contrib import admin
from order.models import Address, Order, OrderItem

admin.site.register(Address)
admin.site.register(Order)
admin.site.register(OrderItem)