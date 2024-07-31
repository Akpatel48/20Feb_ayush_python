from django import forms
from .models import *
class p_user(forms.ModelForm):
    class Meta():
        model=appointments
        fields='__all__'
        
class doctor(forms.ModelForm):
    class Meta():
        model=doctors
        fields='__all__'
        
        
class logi(forms.ModelForm):
    class Meta():
        model=login
        fields='role','name','email','phone','password'

class appointen(forms.ModelForm):
    class Meta():
        model=appointments
        fields='__all__'