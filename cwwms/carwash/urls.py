from django.urls import path

from .views import create_vehicle

urlpatterns = [
    path('vehicles/create', create_vehicle, name='create-vehicle')
]