from django.urls import path
from .views import FoodView


urlpatterns = [
    path("getFood" ,FoodView.as_view(), name="getFood")
]