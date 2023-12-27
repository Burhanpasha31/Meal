from django.contrib import admin
from .models import is_seller,is_customer,MyUser
# Register your models here.

admin.site.register(is_seller)
admin.site.register(is_customer)
admin.site.register(MyUser)


