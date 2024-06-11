from django import forms
from .models import *

class stunde(forms.ModelForm):
    class Meta:
        model=stundet
        fields='__all__'
        
