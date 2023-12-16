from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Payment, Billing, Transaction
from .serializers import PaymentSerializer, BillingSerializer, TransactionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def payment_list(request):
    if request.method == 'GET':
        payments = Payment.objects.all()
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def payment_detail(request, pk):
    payment = get_object_or_404(Payment, pk=pk)
    
    if request.method == 'GET':
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = PaymentSerializer(payment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Similar views can be created for Billing and Transaction models.
