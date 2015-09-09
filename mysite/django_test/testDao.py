
from .models import TestModel
from django.db import DatabaseError

class TestDao(object) :
    def addTest(slef,fromValue = None):
        try:
            raise DatabaseError(500, reasion="DatabaseError")
            test = TestModel.objects.get_or_create(testKey = fromValue.cleaned_data['testKey'], testValue = fromValue.cleaned_data['testValue'], testTitle = fromValue.cleaned_data['testTitle'])
        except:
            raise DatabaseError
        return test
