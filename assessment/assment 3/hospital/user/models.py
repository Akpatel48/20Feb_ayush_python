from django.db import models

# Create your models here.

class login(models.Model):
    name=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=16)
    def __str__(self):
        return self.name
 
class doctors(models.Model):
    logo=models.ImageField(upload_to='static/images/doctor')
    name=models.CharField(max_length=100)
    email=models.EmailField( max_length=254)
    specialities=models.CharField(max_length=50)
    degree=models.CharField(max_length=30)
    experience=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name.name

class appointments(models.Model):
    #userid=models.EmailField()
    user=models.CharField(max_length=100)
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    gender=models.CharField(max_length=10)
    phone=models.BigIntegerField()
    dob=models.DateField()
    address=models.CharField(max_length=100)
    note=models.CharField(max_length=100)

class time(models.Model):
    dname=models.CharField(max_length=100)
    user=models.CharField(max_length=100)
    date=models.DateField(auto_now=False, auto_now_add=False)
    time=models.TimeField(auto_now=False, auto_now_add=False)