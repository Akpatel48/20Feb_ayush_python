from rest_framework import serializers
from .models import *

class stu(serializers.ModelSerializer):
    class Meta:
        models=stude_info
        fildes='__all__'