from django.contrib import admin
from .models import *
# Register your models here.

class prodec(admin.ModelAdmin):
    list_display=['id','p_name']
admin.site.register(prodect,prodec)

class sub_proc(admin.ModelAdmin):
    list_display=['id','p_name','p_price','p_img','p_model','p_ram']
admin.site.register(sub_prodct,sub_proc)
