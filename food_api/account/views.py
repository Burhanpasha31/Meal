# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status 
from .models import is_seller, is_customer
from .serializers import is_sellerSerializer, is_customerSerializer

class is_sellerView(APIView):
    def post(self, request, format=None):
        serializer = is_sellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("done", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        sellers = is_seller.objects.all()
        serializer = is_sellerSerializer(sellers, many=True)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        seller = is_seller.objects.get(id=id)
        serializer = is_sellerSerializer(seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("done", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        seller = is_seller.objects.get(id=id)
        seller.delete()
        return Response("deleted", status=status.HTTP_204_NO_CONTENT)

class is_customerView(APIView):
    def post(self, request, format=None):
        serializer = is_customerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("done", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        customers = is_customer.objects.all()
        serializer = is_customerSerializer(customers, many=True)
        return Response(serializer.data)

    def put(self, request, id, format=None):
        customer = is_customer.objects.get(id=id)
        serializer = is_customerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("done", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        customer = is_customer.objects.get(id=id)
        customer.delete()
        return Response("deleted", status=status.HTTP_204_NO_CONTENT)
