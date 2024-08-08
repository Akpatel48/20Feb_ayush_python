from rest_framework import serializers
from .models import *

class books(serializers.ModelSerializer):
    class Meta():
        model=book
        fields='__all__'
