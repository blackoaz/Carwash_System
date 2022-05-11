from django.urls import path
from .views import create_vehicle, VehicleList, ServiceList

urlpatterns = [
    path('vehicles/', VehicleList.as_view(), name='create-list-vehicle'),
    path('services/', ServiceList.as_view(), name='create-list-service'),
]