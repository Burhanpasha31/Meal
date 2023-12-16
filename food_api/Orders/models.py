from django.db import models

# Create your models here.
# model

class Address(models.Model):
    customer_id =models.ForeignKey('auth.User', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)


    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state} {self.zip_code}, {self.country}"
 # Other fields related to adress details can be added here
