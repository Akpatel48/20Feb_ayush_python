from django.db import models

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    phone=models.BigIntegerField()
    date=models.DateField()
    