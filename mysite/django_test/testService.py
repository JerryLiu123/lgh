# coding:utf-8

from django.db import transaction
from .testDao import TestDao
from django.db import DatabaseError
import logging
from tasks.tasks import test
'''
业务逻辑层，虽然Django将其写在view中，但是那样感觉不利于代码重利用
将所有的功能都在一个方法中实现~~感觉不好
'''
class TestService(object):
    @transaction.non_atomic_requests
    def addTest(self,testModel=None):
        #队列练习
        test.delay(2, 2)
        try:
            while transaction.atomic():#进行事务处理
                if testModel == None:
                    return None
                else:
                    value = None
                    try:
                        value = TestDao().addTest(testModel)
                    except Exception as e:
                        print("---------------  %s  ---------" %e)
                        raise DatabaseError
                    return value
        except:
            raise transaction.TransactionManagementError
        return None
