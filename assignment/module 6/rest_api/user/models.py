from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=100)
    publisher=models.CharField(max_length=100)