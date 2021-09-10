from django.db import models
import datetime

# Create your models here.


class Category(models.Model):
   name = models.CharField(max_length=200)
   status = models.BooleanField(default=True)
   create_at = models.DateTimeField(auto_now=True)



class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    description = models.TextField(max_length=500, default="")
    qty = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)



class SliderImages(models.Model):  
   #  category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/slider') 
    text_on_image =  models.CharField(max_length=256, default="", blank=True, null=True)  
    sub_text_on_image =  models.CharField(max_length=256, default="", blank=True, null=True)  
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)
    


