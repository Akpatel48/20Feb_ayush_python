from django import forms
from .models import *

class inf(forms.ModelForm):
    class Meta:
        model=re
        fields='__all__'