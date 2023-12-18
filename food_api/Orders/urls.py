from django.urls import path
from .views import Order,OrdersDataGenericsView,address,AddressDataGenericsView

urlpatterns = [
    path('OrdersData', Order.as_view(),name='OrdersData' ),
    path('OrdersRetrieve/<int:pk>', OrdersDataGenericsView.as_view(),name='OrdersRetrieve' ),
    path('AddressData', address.as_view(),name='AddressData' ),
    path('AddressRetrieve/<int:pk>', AddressDataGenericsView.as_view(),name='AddressRetrieve' ),
]
