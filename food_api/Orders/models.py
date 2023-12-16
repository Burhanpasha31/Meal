from django.db import models
import uuid

# Create your models here.
# class Orders(models.Model):
#     Order_ID=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
#     Delivery_Address_ID=models.ForeignKey(Address, on_delete=models.CASCADE)
#     # Customer_ID=models.ForeignKey()
#     # Restaurant_ID=models.ForeignKey()
#     # Order_Date=import from payments timestamp
#     # Total_Items=
#     Total_Amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def calculate_total_amount(self):
#         Total_Amount = sum(item.quantity * item.food.price for item in self.orderitem_set.all())
#         self.Total_Amount = Total_Amount
#         return Total_Amount
    
#     def save(self, *args, **kwargs):
#         self.calculate_total_amount()
#         super().save(*args, **kwargs)
    
#     # Payment_status= import from billing model

#     def __str__(self):
#         return str(self.Order_ID)
    

