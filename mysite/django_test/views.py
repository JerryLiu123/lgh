# coding:utf-8 from django.shortcuts import render
from django.http import JsonResponse
# from django.http import HttpResponse
from .forms import AddFrom
from django.core.paginator import Paginator
from .models import TestModel
from django.db import transaction
import logging
# import json
from .testService import TestService
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.http import Http404
from tasks.tasks import test as tasks_test#队列
from helpers.cache import read_from_cache, write_to_cache #缓存

'''
2015年5月21日 15:48:17
lgh
数据库操作,ajax,事务,admin,log,分页,forms

接收页面信息，并转发信息
'''

@transaction.non_atomic_requests
#@cache_page(60 * 15)#设置缓存时间
def testView(request):
    log=logging.getLogger('test1')#说明在使用那个logging:
    test = {}
    #队列练习
    tasks_test.delay(2, 2)
    #缓存
    if not read_from_cache("myKey"):
        value = {"name":"test"}
        write_to_cache("myKey", value, 600)
    else:
        print(read_from_cache("myKey"))
	
    if request.method == 'POST':  #判断传递方式是否为POST
        fromValue = AddFrom(request.POST)
        if fromValue.is_valid():  #验证输入数据是否合法
            try:
                test = TestService().addTest(fromValue)
                #with transaction.atomic():
                #	test = TestModel.objects.get_or_create(testKey = fromValue.cleaned_data['testKey'], testValue = fromValue.cleaned_data['testValue'], testTitle = fromValue.cleaned_data['testTitle'])
                log.info("用户添加记录")
                print(test)
                return JsonResponse(u"添加成功", safe=False)
            except:
                return JsonResponse(u"添加失败", safe=False)
        else:
            return JsonResponse(u"数据输入错误", safe=False)
    else:
        pass
    return render(request, 'test.html', {'listK': test, })  #返回到一另个页面

