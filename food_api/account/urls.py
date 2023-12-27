from django.urls import path
from .views import is_sellerView,is_customerView
urlpatterns = [
    path('getseller/', is_sellerView.as_view(), name='getseller'),
    path('getcustomer/', is_customerView.as_view(), name='getcustomer'),

]