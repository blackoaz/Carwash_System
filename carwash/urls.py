from django.urls import path
from .views import CategoryList, CategoryDetail, VehicleList, VehicleDetail, ServiceList, ServiceDetail #SaleList, SaleDetail
from carwash import views

urlpatterns = [
    #path('categories/', CategoryList.as_view(), name='create-list-category'),
    #path('categories/<int:pk>', CategoryDetail.as_view(), name='get-update-delete-category'),
    #path('vehicles/', VehicleList.as_view(), name='create-list-vehicle'),
    #path('vehicles/<int:pk>', VehicleDetail.as_view(), name='get-update-delete-vehicle'),
    #path('services/', ServiceList.as_view(), name='create-list-service'),
    #path('services/<int:pk>', ServiceDetail.as_view(), name='get-update-delete-service'),
    #path('sales/', SaleList.as_view(), name='create-list-sale'),
    #path('sales/<int:pk>', SaleDetail.as_view(), name='get-update-delete-sale'),
    path('home/',views.home, name ='home'),
    path('carwash/', views.index, name = 'carwash'),
    path('create_sale', views.create_sale, name = 'create_sale'),
    path('more_vehicles/', views.recent, name = 'recentWash'),
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
    

"""
    #Api urls
    path('vehicles/', views.vehicleApiView.as_view()),
    path('vehicle_update/<int:pk>/', views.vehicletDetail.as_view()),
    path('categories/', views.CategoryApiView.as_view()),
    path('category_update/<int:pk>/', views.CategoryDetail.as_view()),
    path('services/', views.ServiceApiView.as_view()),
    path('service_update/<int:pk>/', views.ServiceDetail.as_view()),
    path('saleitem/', views.SaleItemApiView.as_view()),
    path('saleitem_update/<int:pk>/', views.SaleItemDetail.as_view()),
    path('sale/', views.SaleApiView.as_view()),
    path('sale_update/<int:pk>/', views.SaleDetail.as_view()),"""
