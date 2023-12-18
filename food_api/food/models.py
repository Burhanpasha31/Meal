from django.db import models
from account.models import is_customer , MyUser
# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
      return self.name



class Favorite(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE) 
    favorite = models.CharField(max_length=50)

    def __str__(self):
        return str(self.food)
    

class CartItem(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    food = models.ForeignKey('Food', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.food.name} for {self.user.name}"