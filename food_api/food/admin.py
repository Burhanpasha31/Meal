from django.contrib import admin
from .models import Food,Favorite,CartItem

# Register your models here.
admin.site.register(Food)
admin.site.register(Favorite)
admin.site.register(CartItem)
