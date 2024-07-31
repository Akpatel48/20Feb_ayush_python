from django.contrib import admin
from .models import *
# Register your models here.


class stude(admin.ModelAdmin):
    list_display=['name','age','phone']
admin.site.register(stude_info,stude)