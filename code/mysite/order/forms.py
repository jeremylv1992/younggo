# coding=utf-8
from django import forms
from order.models import Address

class AddressForm(forms.ModelForm):
    '''
    @summary: 验证地址表单
    '''
    class Meta:
        model = Address
        fields = ('name', 'tel', 'second_tel', 'addr',)
    
    
        
    
    
