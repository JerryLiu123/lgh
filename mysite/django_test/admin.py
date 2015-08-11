from django.contrib import admin
from .models import TestModel 
#Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(TestModel,AuthorAdmin)
