from django import forms
from .models import *

class NameForm(forms.ModelForm):
    # name = forms.CharField(max_length = 100, label = 'Name')
    # course = forms.CharField(max_length=100, label= 'Course')
    class Meta:
        model = Restaurant
        fields ='__all__'