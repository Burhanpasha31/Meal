from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import Response
from .models import Food
from .serializers import FoodSerializers
# Create your views here.

class FoodView(APIView):
    


    def post(self, request,format=None):
        pass

    def get(self, request,format=None):
        food = Food.objects.all()
        serializer = FoodSerializers(food, many=True)
        print(serializer)
        return Response(serializer.data)
        pass

    def put(self, request,format=None):
        pass

    def delete(self, request,format=None):
        pass
