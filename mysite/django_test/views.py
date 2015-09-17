# coding:utf-8 from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .forms import AddFrom
from django.core.paginator import Paginator
from .models import TestModel
#from django.db import transaction#事务
import logging
# import json
from .testService import TestService
from django.views.decorators.cache import cache_page
from django.shortcuts import render
from django.http import Http404
from tasks.tasks import test as tasks_test#队列
from helpers.cache import read_from_cache, write_to_cache #缓存
#import xlwt#Excel操作
import re
from django.utils.encoding import smart_str
from .utils.dowExcel import doDowExcel
'''
2015年5月21日 15:48:17
lgh
数据库操作,ajax,事务,admin,log,分页,forms

接收页面信息，并转发信息
'''

#@transaction.non_atomic_requests#设置 事务
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


def testExcel(request):
    log = logging.getLogger('test1')
    _value=[
            ["0-0","0-1","0-2","0-3","0-4"],
            ["1-0","1-1","1-2","1-3"],
            ["2-0","2-1","2-2","2-3","2-4","2-5","2-6","2-7","2-8"]
            ]
    wb = doDowExcel(sheetName="Sheetname", value=_value)
    fname = 'testfile.xls'
    agent=request.META.get('HTTP_USER_AGENT') 
    if agent and re.search('MSIE',agent):
        response = HttpResponse(content_type='application/vnd.ms-excel') #解决ie不能下载的问题
        response['Content-Disposition'] ='attachment; filename=%s' % fname #解决文件名乱码/不显示的问题
    else:
        response = HttpResponse(content_type='application/ms-excel')#解决ie不能下载的问题
        response['Content-Disposition'] ='attachment; filename=%s' % smart_str(fname) #解决文件名乱码/不显示的问题
    ##########################################保存
    wb.save(response)
    return response
