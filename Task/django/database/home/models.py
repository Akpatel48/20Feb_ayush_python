from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.IntegerField
    dab=models.DateField()
    addres=models.TextField()