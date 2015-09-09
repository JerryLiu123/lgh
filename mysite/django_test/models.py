# coding:utf-8
from django.db import models
#from mongoengine import *
#from django.utils.encoding import python_2_unicode_compatible#兼容python2

# 2015年5月15日 09:19:54
# lgh  

class TestModel(models.Model):
	
    testKey = models.CharField(max_length = 20)
    testValue = models.CharField(max_length = 20)
    testTitle = models.CharField(max_length = 20)
    #指定对象用那个字段表达自己
    def __str__(self):#在python3中使用__str__，在python2中使用__unicode__
        return self.testTitle
#    class Meta:
#		ordering = ['-testKey']


