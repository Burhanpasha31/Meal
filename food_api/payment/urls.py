from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.payment_list, name='payment-list'),
    path('payment/<int:pk>/', views.payment_detail, name='payment-detail'),
    # Add similar paths for Billing and Transaction views if needed
]
