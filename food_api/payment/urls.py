from django.urls import path
from . import views


urlpatterns = [
    path('payment/', views.payment_list, name='payment-list'),
    path('payment/<int:pk>/', views.payment_detail, name='payment-detail'),
    path('transactions/', views.transaction_list, name='transaction-list'),
    path('transactions/<int:pk>/', views.transaction_detail, name='transaction-detail'),
    path('billings/', views.billing_list, name='billing-list'),
    path('billings/<int:pk>/', views.billing_detail, name='billing-detail'),
]