from django.conf import settings
from django.core.cache import cache
import json

#read cache user id
def read_from_cache(valueName):
    key = 'test' + valueName
    value = cache.get(key)
    if value == None:
        data = None
    else:
        data = json.loads(value)
    return data

#write cache user id
def write_to_cache(valueName, value, timeOut=None):
    key = 'test' + valueName
    if timeOut == None:
        timeOut_ = settings.NEVER_REDIS_TIMEOUT
    else:
        timeOut_ = timeOut
    cache.set(key, json.dumps(value), timeOut_)
    return True
