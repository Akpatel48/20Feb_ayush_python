from django.contrib import admin
from .models import *
# Register your models here.
class studet(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','name','email','phone','dab','address']

admin.site.register(stundet,studet)