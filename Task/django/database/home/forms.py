from django import forms
from .models import *

class student(forms.ModelForm):
    class Meta:
        model=student
        filed='__all__'