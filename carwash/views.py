
from ast import If
from multiprocessing import context
from unicodedata import category
from urllib import request
import uuid
from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import auth,messages
# Create your views here.
from .serializers import CategorySerializer,ServiceSerializer, VehicleSerializer
from .models import CarwashSale, Category,Service, Staff, Vehicle
from users.models import CustomUser
from .forms import *
from django.contrib.auth.forms import UserCreationForm




def home(request):           
        return render(request,'home.html') 

def main(request):
    return render(request,'index.html')

def index(request):
    categories = Category.objects.all()
    vehicle = Vehicle.objects.all()
    services = Service.objects.all()
    sales = CarwashSale.objects.filter(Payment_status='Unpaid')[0:2]
    staffs = Staff.objects.all()
    form = VehicleForm() 
    form = CarwashSaleForm() 

    context = {'categories':categories,'services':services,'sales':sales,'staffs':staffs,'vehicles':vehicle,'form':form,'form':form}
    return render(request,'carwashsys.html',context)

def create_sale(request):
    
    if request.method == 'POST':
        vehicle = request.POST['vehicle']
        Category = request.POST['Category']
        Service = request.POST['Service']
        Staff = request.POST['Staff']
        payment_status = request.POST['Payment_status']

        sale = CarwashSale(vehicle=vehicle,category=Category,service=Service,staff=Staff,Payment_status=payment_status)
        sale.save()
        messages.info(request,'Sale Added successfully')
        return redirect('carwash')
    return render(request,'carwashsys.html')    






def recent(request):
    sales = CarwashSale.objects.filter(Payment_status='Unpaid')
    context = {'sales':sales}
    return render(request,'recent.html',context)

def body_type(request):
    categories = Category.objects.all()
    context = {'categories':categories,}
    return render(request,'body_type.html',context)

def services(request):
    services = Service.objects.all()
    context = {'services':services,}
    return render(request,'services.html',context)

def vehicles(request):
    vehicle = Vehicle.objects.all()
    context = {'vehicles':vehicle}
    return render(request,'vehicles.html',context)

def users(request):
    users = CustomUser.objects.all()
    context = {'users':users,}
    return render(request,'users.html',context)

#CRUD OPERATIONS FOR VEHICLE BODY
def create_body(request):
    form = CategoryForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('body_type')

    context = {'form':form}
    return render(request,'createbody.html',context)

def update_body(request, pk):

    category = Category.objects.get(id=pk)
    form = CategoryForm(instance=category)
    form = CategoryForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('body_type')
    context = {'form':form}
    return render (request,'createbody.html',context)

def delete_body(request, pk):
    category = Category.objects.get(id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('body_type')
    context = {'category':category}
    return render(request, 'deletebody.html',context)

#CRUD operations for Users
def createUser(request):
    form = CustomUserForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')

    context = {'form':form}
    return render(request,'createUser.html',context)

def updateUser(request, pk):

    user = CustomUser.objects.get(id=pk)
    form = CustomUserForm(instance=user)
    form = CustomUserForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = CustomUserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {'form':form}
    return render (request,'updateUser.html',context)

def deleteUser(request, pk):
    user = CustomUser.objects.get(id=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {'user':user}
    return render(request, 'deleteUser.html',context)

#CRUD operations for Service
def createService(request):
    form = ServiceForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('services')
    context = {'form':form}
    return render(request,'createService.html',context)

def updateService(request, pk):
    service = Service.objects.get(uid=pk)
    form = ServiceForm(instance=service)
    form = ServiceForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = ServiceForm(request.POST,instance=service)
        if form.is_valid():
            form.save()
            return redirect('services')
    context = {'form':form}
    return render (request,'updateService.html',context)  


def deleteService(request, pk):
    service = Service.objects.get(uid=pk)
    if request.method == 'POST':
        Service.delete()
        return redirect('services')
    context = {'service':service}
    return render(request, 'deleteService.html',context)      
    

#CRUD Operations for Vehicles registered
def updateVehicle(request, pk):

    vehicle = Vehicle.objects.get(id=pk)
    form = VehicleForm(instance=vehicle)
    form = VehicleForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = VehicleForm(request.POST,instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicles')
    context = {'form':form}
    return render (request,'updateVehicle.html',context)

def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicles')
    context = {'vehicle':vehicle}
    return render(request, 'deleteVehicle.html',context)

#sale
# def register_vehicle(request):
#     form = VehicleForm()
#     if request.method == 'POST':
#         form = VehicleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request,'vehicle created successfully proceed payment')
#         elif form is not None:
#             messages.info(request,'vehicle already exist or does not comply with Registration Format')    
#         return redirect('carwash')
#     context = {'form':form}               
#     return render(request,'carwashsys.html',context) 


# def register_sale(request):
#     form = CarwashSaleForm()        
#     if request.method == 'POST':
#         form = CarwashSaleForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.info(request,'Sale Registered successfully')   
#             return redirect('carwash')
#     context = {'form':form}               
#     return render(request,'carwashsys.html',context) 

#user registration and login
def registerUser(request):
    form = CustomUserForm()

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request,'Account was created for ' + " " + user)
            return redirect ('login')
    context = {'form':form}
    return render(request,'registerUser.html',context) 


def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
       

        if user is not None: 
            login(request,user)
            return redirect('main_menu')
        else:
            messages.info(request,'Username or Password is incorrect')    
        
    context = {}
    return render(request,'login.html',context)

def logOut(request):
    logout(request)
    return redirect('loginPage')


    





















#classbased view
class vehicleApiView(APIView):

    def get(self,request):
        Vehicles = Vehicle.objects.all()
        serializer = VehicleSerializer(Vehicles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class vehicletDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Vehicle = self.get_object(pk)
        serializer = VehicleSerializer(Vehicle)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Vehicle = self.get_object(pk)
        serializer = VehicleSerializer(Vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Vehicle = self.get_object(pk)
        Vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#Category API
class CategoryApiView(APIView):

    def get(self,request):
        Categories = Category.objects.all()
        serializer = CategorySerializer(Categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Vehicle = self.get_object(pk)
        serializer = CategorySerializer(Vehicle, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Service Api
class ServiceApiView(APIView):

    def get(self,request):
        services = Service.objects.all()
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class ServiceDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = ServiceSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Service = self.get_object(pk)
        serializer = ServiceSerializer(Service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Service = self.get_object(pk)
        Service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""Sale item
class SaleItemApiView(APIView):

    def get(self,request):
        saleItem = SaleItem.objects.all()
        serializer = SaleItemSerializer(saleItem, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaleItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class SaleItemDetail(APIView):
    
#Retrieve, update or delete a snippet instance.
   def get_object(self, pk):
        try:
            return SaleItem.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        SaleItem = self.get_object(pk)
        serializer = SaleItemSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        SaleItem = self.get_object(pk)
        serializer = SaleItemSerializer(Service, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        SaleItem = self.get_object(pk)
        SaleItem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#sale API
class SaleApiView(APIView):

    def get(self,request):
        sale = Sale.objects.all()
        serializer = SaleSerializer(sale, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class SaleDetail(APIView):

    #Retrieve, update or delete a snippet instance.

    def get_object(self, pk):
        try:
            return Sale.objects.get(pk=pk)
        except Sale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Sale = self.get_object(pk)
        serializer = SaleSerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Sale = self.get_object(pk)
        serializer = SaleSerializer(Sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Sale = self.get_object(pk)
        Sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""
#Generics based API
#CreateView, UpdateView, DeleteView, ListView, DetailView

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
"""class SaleList(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer"""

