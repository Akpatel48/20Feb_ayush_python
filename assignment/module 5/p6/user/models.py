from django.db import models

# Create your models here.
class prodect(models.Model):
    p_name=models.CharField(max_length=50)

class sub_prodct(models.Model):
    p_name=models.ForeignKey(prodect,on_delete=models.CASCADE)
    p_price=models.IntegerField()
    p_img=models.ImageField()
    p_model=models.CharField(max_length=50)
    p_ram=models.CharField(max_length=30)