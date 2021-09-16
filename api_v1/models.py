from django.db import models
import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password

# Create your models here.






class Category(models.Model):
   name = models.CharField(max_length=200)
   status = models.BooleanField(default=True)
   create_at = models.DateTimeField(auto_now=True)

   def __str__(self):
       return self.name



class Products(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static/', blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField(max_length=500, default="")
    qty = models.IntegerField()
    in_stock = models.BooleanField(default=True)
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    



class SliderImages(models.Model):  
   #  category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/slider', blank=True, null=True) 
    text_on_image =  models.CharField(max_length=256, default="", blank=True, null=True)  
    sub_text_on_image =  models.CharField(max_length=256, default="", blank=True, null=True)  
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)


class OrderItem(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    qty = models.IntegerField()
    total = models.IntegerField()
    payment_method: models.CharField(max_length=256, default="COD", blank=True, null=True)
    is_pay: models.BooleanField(default=False)
    shipping_address =  models.TextField(max_length=1000, default="")
    status = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now=True)


class User_M(AbstractUser):
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = []
   image = models.ImageField(upload_to='profile/', blank=True, null=True)
   email = models.EmailField(unique=True)
   mobile_no = models.CharField(max_length=20, default="", blank=True, null=True)
   password = models.CharField(max_length=30)
   status = models.BooleanField(default=True)
   create_at = models.DateTimeField(auto_now=True)
   username =models.CharField(max_length=500,default="", blank=True, null=True)


   def __str__(self):
       return self.email




    
    


