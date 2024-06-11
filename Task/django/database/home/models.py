from django.db import models

# Create your models here.
class stundet(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.IntegerField()
    dab=models.DateField()
    address=models.TextField()
    