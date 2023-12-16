from django.contrib import admin
from .models import Payment, Billing, Transaction

# Register your models here.
admin.site.register(Payment)
admin.site.register(Billing)
admin.site.register(Transaction)