from rest_framework import serializers
from .models import Products, Category, SliderImages, User_M


class NewUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_M
        fields = '__all__'



class SliderImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderImages
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'        