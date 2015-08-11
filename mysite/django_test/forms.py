from django import forms

class AddFrom(forms.Form):
    testKey = forms.IntegerField()
    testValue = forms.CharField()
    testTitle = forms.CharField()
