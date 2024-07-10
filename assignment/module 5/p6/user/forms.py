from django import forms
from .models import *

class prodec(forms.ModelForm):
    class Meta():
        model=prodect
        fields='__all__'
        
class sub_prodec(forms.ModelForm):
    class Meta():
        model=sub_prodct
        fields='__all__'