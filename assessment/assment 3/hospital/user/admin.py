from django.contrib import admin
from .models import *   
# Register your models here.


class doctor(admin.ModelAdmin):
    list_display=['id','name','specialities','degree','experience','gender','age','logo']

class use(admin.ModelAdmin):
    list_display=['id','name','age','gender','dob','email']

class logi(admin.ModelAdmin):
    list_display=['id','role','name','email','phone','password']

'''class tim(admin.ModelAdmin):
    list_display=['dname','time','date']'''
admin.site.register(time)
admin.site.register(appointments)
admin.site.register(doctors,doctor)
admin.site.register(login,logi)