from django.db import models

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    dob=models.DateField()
    email=models.EmailField()
    password=models.CharField(max_length=30)

class doctors(models.Model):
    name=models.CharField(max_length=50)
    specialities=models.CharField(max_length=50)
    degree=models.CharField(max_length=30)
    experience=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    logo=models.ImageField()
	
class login(models.Model):
    role=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=16)
 