from django.contrib import admin
from .models import Category, Products, SliderImages, NewUser, OrderItem

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)
admin.site.register(SliderImages)
admin.site.register(NewUser)
admin.site.register(OrderItem)
