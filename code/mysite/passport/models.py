# coding=utf-8
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name=u"用户")
    GENDER_CHOICES = (('M','Man'),
                      ('W','Woman'),
                      ('U', 'Unknown'))
    gender = models.CharField(u"性别", max_length=1, 
                              choices=GENDER_CHOICES, default='U')
    
    def __unicode__(self):
        return u"%s" %(self.user)
    
