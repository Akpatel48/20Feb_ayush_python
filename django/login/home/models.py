from django.db import models

# Create your models here.
class re(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    mobile=models.IntegerField()