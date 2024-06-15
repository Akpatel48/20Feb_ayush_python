from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class logi(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.BigIntegerField()
    password=models.CharField(max_length=50)

    