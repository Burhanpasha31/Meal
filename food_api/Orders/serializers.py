from rest_framework import serializers
from .models import Orders,Address

class OrdersSerializer(serializers.ModelSerializer):

    class Meta:
        model= Orders
        fields="__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address
        fields="__all__"