from django.db import models
from account.models import MyUser
# Create your models here.

class Payment(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)  # To store payment method (e.g., PayTm, UPI, Cards, Netbanking)
    timestamp = models.DateTimeField(auto_now_add=True)

    # Other fields related to payment details can be added here
    
    
class Billing(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    # Other fields related to billing information can be added here
    

class Transaction(models.Model):
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE)
    billing = models.ForeignKey('Billing', on_delete=models.CASCADE)
    success = models.BooleanField(default=False)
    # response_data = models.JSONField()  # Store response data from payment gateway

    # Other fields related to transaction details can be added here





