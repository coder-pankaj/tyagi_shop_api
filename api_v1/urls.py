
from django.contrib import admin
from django.urls import path
from .views import ProductApiView, SliderImageApiView, ProductsApiView

urlpatterns = [
    path('products/', ProductsApiView.as_view()),
    path('product/<int:pk>', ProductApiView.as_view()),
    path('slider/', SliderImageApiView.as_view())
]
