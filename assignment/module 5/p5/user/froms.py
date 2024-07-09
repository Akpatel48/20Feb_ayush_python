from django import forms
from .models import *

class userdata(forms.ModelForm):
    class Meta:
        model = data
        fields = '__all__'