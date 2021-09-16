
from django.contrib import admin
from django.urls import path
from .views import ProductApiView, SliderImageApiView, ProductsApiView, NewUserApiView, LoginApiView

urlpatterns = [
    path('login/', LoginApiView.as_view()),
    path('register/', NewUserApiView.as_view()),
    path('products/', ProductsApiView.as_view()),
    path('product/<int:pk>', ProductApiView.as_view()),
    path('slider/', SliderImageApiView.as_view())
]
