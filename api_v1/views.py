from django.shortcuts import render
from rest_framework.response import Response
from .serializer import ProductSerializer, CategorySerializer, SliderImagesSerializer, NewUserSerializer
from .models import Products, Category, SliderImages, User_M
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password, check_password



# Create your views here.

def create_get_Token(user):
    try:
        token = Token.objects.get(user_id=user.id)
        return token.key
    except Token.DoesNotExist:
        token = Token.objects.create(user=user)
        return token.key

class LoginApiView(APIView):

    def post(self, request):
        try:
         user = User_M.objects.get(email=request.data['email'])
         serializer = User_MSerializer(user)
        except User_M.DoesNotExist:
            result = {
                "result": '',
                "status": status.HTTP_404_NOT_FOUND,
                "message": "No such user exist, please contact to admin"
            }
            return Response(result, status=status.HTTP_404_NOT_FOUND)

        flag = check_password(user.password, request.data['password'])
        token = create_get_Token(user)
        result = {
        "result":serializer.data,
        "token":token,
        "status":status.HTTP_200_OK,
        "message":"user find successfully"
        }
        return Response(result, status=status.HTTP_200_OK)



class NewUserApiView(APIView):
    def post(self, request):
        serializer = NewUserSerializer(data = request.data)
        if serializer.is_valid():
            password = make_password(request.data['password'])
            serializer.save(password=password)
            user = User_M.objects.get(email=serializer.data['email'])
            token = create_get_Token(user)
            result = {
                "result":serializer.data,
                "token":token,
                "status":status.HTTP_201_CREATED,
                "message":"User register successfully."
            }
            return Response(result, status=status.HTTP_201_CREATED)
        result = {
            "result": serializer.errors,
            "status": status.HTTP_400_BAD_REQUEST,
            "message": "something went wrong"
        }
        return Response(result, status=status.HTTP_400_BAD_REQUEST)



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





