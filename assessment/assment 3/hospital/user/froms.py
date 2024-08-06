from django import forms
from .models import *
        
class doctor(forms.ModelForm):
    class Meta():
        model=doctors
        fields='__all__'
        
class tim(forms.ModelForm):
    class Meta():
        model=time
        fields='__all__'
        
class logi(forms.ModelForm):
    class Meta():
        model=login
        fields='role','name','email','phone','password'

class appointen(forms.ModelForm):
    class Meta():
        model=appointments
        fields='__all__'