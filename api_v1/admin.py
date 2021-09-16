from django.contrib import admin
from .models import Category, Products, SliderImages, User_M, OrderItem

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SliderImages)
admin.site.register(User_M)
admin.site.register(OrderItem)
