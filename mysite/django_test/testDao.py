
from .models import TestModel

class TestDao(object):
    def addTest(slef,fromValue = None):
        test = TestModel.objects.get_or_create(testKey = fromValue.cleaned_data['testKey'], testValue = fromValue.cleaned_data['testValue'], testTitle = fromValue.cleaned_data['testTitle'])
        return test
