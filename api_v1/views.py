from django.shortcuts import render
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer, SliderImagesSerializer
from .models import Products, Category, SliderImages
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.




class ProductsApiView(APIView):
    def get(self, request):
        product = Products.objects.all()
        serializer = ProductSerializer(product, many=True)
        result = {
            "result":serializer.data,
            "status":status.HTTP_200_OK,
            "message":"data find successfully"
        }
        return Response(result, status=status.HTTP_200_OK)

class ProductApiView(APIView):
    def get(self, request,pk):
        try:
             product = Products.objects.get(pk=pk)
        except Products.DoesNotExist:
            result = {
            "result":[],           
            "status":status.HTTP_204_NO_CONTENT,
            "message":"No such product exist, please contact to admin"
        }
            return Response(result, status=status.HTTP_200_OK)

        serializer = ProductSerializer(product)
        result = {
            "result":serializer.data,
            "status":status.HTTP_200_OK,
            "message":"data find successfully"
        }
        return Response(result, status=status.HTTP_200_OK)
        
class SliderImageApiView(APIView):
    def get(self, request):
        slider_image = SliderImages.objects.all()
        serializer = SliderImagesSerializer(slider_image, many=True)
        result = {
            "result":serializer.data,
            "status":status.HTTP_200_OK,
            "message":"data find successfully"

        }
        return Response(result, status=status.HTTP_200_OK)





