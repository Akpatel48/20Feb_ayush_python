from django import forms
from .models import *

class re(forms.ModelForm):
    class Meta:
        model=logi
        fields='__all__'
class ot(forms.ModelForm):
    class Meta:
        model=otp
        fields='__all__'