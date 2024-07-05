from django import forms
from .models import *
class p_user(forms.ModelForm):
    class Meta():
        model=user
        fields='__all__'
        
class doctor(forms.ModelForm):
    class Meta():
        model=doctors
        fields='__all__'
        
        
class logi(forms.ModelForm):
    class Meta():
        model=login
        fields='role','name','email','phone','password'