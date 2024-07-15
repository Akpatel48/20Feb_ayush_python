from django.db import models

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    inquiry=models.CharField(max_length=100)
    message=models.TextField()
    
    
class usinup(models.Model):
    name=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    email=models.EmailField()
    password=models.CharField(max_length=16)

class img(models.Model):
    image=models.ImageField(upload_to='static/img/image', height_field=None, width_field=None, max_length=None)
    name=models.CharField(max_length=100)
    width=models.IntegerField()
    height=models.IntegerField()
    tags=models.CharField(max_length=200)
    time=models.DateField(auto_now=True, auto_now_add=False)