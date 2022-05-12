from django.urls import path
from .views import CategoryList, CategoryDetail, VehicleList, VehicleDetail, ServiceList, ServiceDetail, SaleList, SaleDetail

urlpatterns = [
    path('categories/', CategoryList.as_view(), name='create-list-category'),
    path('categories/<int:pk>', CategoryDetail.as_view(), name='get-update-delete-category'),
    path('vehicles/', VehicleList.as_view(), name='create-list-vehicle'),
    path('vehicles/<int:pk>', VehicleDetail.as_view(), name='get-update-delete-vehicle'),
    path('services/', ServiceList.as_view(), name='create-list-service'),
    path('services/<int:pk>', ServiceDetail.as_view(), name='get-update-delete-service'),
    path('sales/', SaleList.as_view(), name='create-list-sale'),
    path('sales/<int:pk>', SaleDetail.as_view(), name='get-update-delete-sale'),
]