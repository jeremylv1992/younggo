# coding=utf-8
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from passport.models import UserProfile

def add_user_profile(sender, instance, created, **kwargs):
    '''
    @summary: 信号处理器，在django user创建后，立即添加
    '''
    if created:
        UserProfile.objects.create(user=instance)
        instance.save()

post_save.connect(add_user_profile, sender=User)

    
