from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Orders,Address
from .serializers import OrdersSerializer,AddressSerializer

# Create your views here.

class Order(generics.ListCreateAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer

class OrdersDataGenericsView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Orders.objects.all()
    serializer_class = OrdersSerializer

class address(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class AddressDataGenericsView(generics.RetrieveUpdateDestroyAPIView):
    queryset= Address.objects.all()
    serializer_class = AddressSerializer
