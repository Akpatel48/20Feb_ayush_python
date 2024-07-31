from rest_framework import serializers
from .models import *
class stude(serializers.ModelSerializer):
    class Meta:
        model=stude_info
        fields='__all__'