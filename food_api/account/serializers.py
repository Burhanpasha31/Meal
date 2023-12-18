
from rest_framework import serializers
from .models import is_seller,is_customer

class is_sellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = is_seller
        # fields = ["name","email","phone"]
        fields = "__all__"
class is_customerSerializer(serializers.ModelSerializer):
    class Meta:
        model = is_customer
        # fields = ["name","email","phone"]
        fields = "__all__"