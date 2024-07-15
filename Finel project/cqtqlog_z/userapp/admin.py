from django.contrib import admin
from .models import *
# Register your models here.

class contac(admin.ModelAdmin):
    list_display=['id','name','email','inquiry','message']

admin.site.register(contact,contac)
admin.site.register(img)