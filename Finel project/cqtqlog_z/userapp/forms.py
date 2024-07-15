from django import forms
from .models import *


class inquiry(forms.ModelForm):
    class Meta():
        model=contact
        fields='__all__'
        
class sinu(forms.ModelForm):
    class Meta():
        model=usinup
        exclude =['image','name','width','height','tags']