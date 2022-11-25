from django.urls import path
from .views import *
from carwash import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
#API URLS
# path('categories/', CategoryList.as_view(), name='create-list-category'),
# path('categories/<str:pk>', CategoryDetail.as_view(), name='get-update-delete-category'),
# path('vehicles/', VehicleList.as_view(), name='create-list-vehicle'),
# path('vehicles/<str:pk>', VehicleDetail.as_view(), name='get-update-delete-vehicle'),
# path('services/', ServiceList.as_view(), name='create-list-service'),
# path('services/<str:pk>', ServiceDetail.as_view(), name='get-update-delete-service'),
# path('sales/', SaleList.as_view(), name='create-list-sale'),
# path('sales/<str:pk>', SaleDetail.as_view(), name='get-update-delete-sale'),
# path('users/', UserList.as_view(), name='create-list-sale'),
# path('users/<str:pk>', UserDetail.as_view(), name='get-update-delete-sale'),
# path('staffs/', StaffList.as_view(), name='create-list-sale'),
# path('staffs/<str:pk>', StaffDetail.as_view(), name='get-update-delete-sale'),
# path('auth/', obtain_auth_token),

#End of API URLS
    path('home/',views.home, name ='home'),
    path('carwash/', views.index, name = 'carwash'),
    path('more_vehicles/', views.recent, name = 'recentWash'),
    path('paid_vehicles/', views.paid_vehicles, name = 'paidVehicles'),
    path('payment/<str:pk>', views.payment, name = 'Payment'),
    path('menu/', views.main, name = 'main_menu'),
    path('body/', views.body_type, name = 'body_type'),
    path('register_sale', views.register_sale, name = 'register_sale'),
    # path('register_vehicle', views.register_vehicle, name = 'register_vehicle'),
    path('services/', views.services, name = 'services'),
    path('vehicles/', views.vehicles, name = 'vehicles'),
    path('users/', views.users, name = 'users'),

    #Crud operations url for Body type
    path('create_body/', views.create_body, name = 'create_body'),
    path('update_body/<str:pk>/', views.update_body, name = 'update_body'),
    path('delete_body/<str:pk>/', views.delete_body, name = 'delete_body'),

    #Crud operations url for Body type
    path('createUser/', views.createUser, name = 'createUser'),
    path('updateUser/<str:pk>/', views.updateUser, name = 'updateUser'),
    path('deleteUser/<str:pk>/', views.deleteUser, name = 'deleteUser'),

    #Crud operations url for Services
    path('createService/', views.createService, name = 'createService'),
    path('updateService/<str:pk>/', views.updateService, name = 'updateService'),
    path('deleteService/<str:pk>/', views.deleteService, name = 'deleteService'),

    #Crud operations url for registered vehicles
    path('updateVehicle/<str:pk>/', views.updateVehicle, name = 'updateVehicle'),
    path('deleteVehicle/<str:pk>/', views.deleteVehicle, name = 'deleteVehicle'),
#User registration and login urls
    path('registerUser/', views.registerUser, name = 'registerUser'),
    path('loginPage/', views.loginPage, name = 'loginPage'),
    path('logout/', views.logOut, name = 'logout'),
 ]

