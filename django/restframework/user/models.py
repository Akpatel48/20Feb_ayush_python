from django.db import models

# Create your models here.
class stude_info(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    phone=models.BigIntegerField()