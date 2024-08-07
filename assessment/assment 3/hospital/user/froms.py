from django import forms
from .models import *
        
class doctorsform(forms.ModelForm):
    class Meta():
        model=doctors
        fields='__all__'
        
class timeform(forms.ModelForm):
    class Meta():
        model=time
        fields='__all__'
        
class loginform(forms.ModelForm):
    class Meta():
        model=login
        fields='role','name','email','phone','password'

class appointenform(forms.ModelForm):
    class Meta():
        model=appointments
        fields='__all__'