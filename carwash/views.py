from ast import If, Return
from multiprocessing import context
from unicodedata import category
from urllib import request
import uuid
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import redirect, render
from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth,messages
# Create your views here.
from .serializers import CategorySerializer,ServiceSerializer, VehicleSerializer,CarwashSaleSerializer,StaffSerializer,UserSerializer
from .models import CarwashSale, Category,Service, Staff, Vehicle
from users.models import CustomUser
from .forms import *
from . filters import *




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

    # if 'q' in request.GET:
    #     q = request.GET['q']
    #     sales = CarwashSale.objects.filter(id__icontains=q)
    # else:
    #    sales = ' '


    context = {'categories':categories,'services':services,'sales':sales,'staffs':staffs,'vehicles':vehicle,'form':form,'form':form}
    return render(request,'carwashsys.html',context)

def recent(request):
    sales = CarwashSale.objects.filter(Payment_status='Unpaid')
    context = {'sales':sales}
    return render(request,'recent.html',context)

def payment(request,pk):
    CarwashSale.objects.filter(uid=pk).update(Payment_status='Paid')
    return redirect('paidVehicles')


def paid_vehicles(request):
    sales = CarwashSale.objects.filter(Payment_status='Paid')
    myFilter = CarwashSaleFilter(request.GET,queryset=sales)
    paginate_by = 10
    context = {'sales':sales,'paginate_by':paginate_by,'myFilter':myFilter}
    return render(request,'paidvehicles.html',context)

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
    form = UserRegistrationForm()
    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')

    context = {'form':form}
    return render(request,'createUser.html',context)

def updateUser(request, pk=0):

    form = UserRegistrationForm()
    user = CustomUser.objects.get(id=pk)
    form = UserRegistrationForm(instance=user)

    if request.method == 'POST':
        #print("printing Post",request.POST)
        form = UserRegistrationForm(request.POST,instance=user)
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
    form = ServiceForm()
    service = Service.objects.get(uid=pk)
    form = ServiceForm(instance=service)
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
def updateVehicle(request, pk=0):
    if request.method == 'GET':
        if id == 0:
            form = VehicleForm()
        else:
            vehicle = Vehicle.objects.get(id=pk)
            form = VehicleForm(instance=vehicle)
        return render (request,'updateVehicle.html',{'form':form})
    else:
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehicles')



def deleteVehicle(request, pk):
    vehicle = Vehicle.objects.get(id=pk)
    if request.method == 'POST':
        vehicle.delete()
        return redirect('vehicles')
    context = {'vehicle':vehicle}
    return render(request, 'deleteVehicle.html',context)


def register_sale(request):
    if request.method == 'GET':
        form = CarwashSaleForm()
        context = {'form':form}
        return render(request,'carwashsys.html',context)
    else:
        form = CarwashSaleForm(request.POST)
        if form.is_valid():
            form.save()
            #messages.info(request,'Sale Registered successfully')
        return redirect('carwash')


#user registration and login
def registerUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserRegistrationForm()

        if request.method == 'POST':
            form = UserRegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                #messages.success[request,'Account was created for ' + " " + user]
                return redirect ('loginPage')
        context = {'form':form}
    return render(request,'registerUser.html',context)


def loginPage(request):
        if request.POST:
            form = UserLoginForm(request.POST)
            if form.is_valid:
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request,username=username,password=password)

                if user is not None:
                    login(request,user)
                    return redirect('carwash')
                #else:
                    #messages.error(request,f'Username or Password is incorrect')

        else:
            form = UserLoginForm()

        context = {'form':form}
        return render(request,'loginpage.html',context)

def logOut(request):
    logout(request)
    return redirect('loginPage')

# API CreateView, UpdateView, DeleteView, ListView, DetailView

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class SaleList(generics.ListCreateAPIView):
    queryset = CarwashSale.objects.all()
    serializer_class = CarwashSaleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CarwashSale.objects.all()
    serializer_class = CarwashSaleSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class StaffList(generics.ListCreateAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class StaffDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]












#classbased view
# class vehicleApiView(APIView):

#     def get(self,request):
#         Vehicles = Vehicle.objects.all()
#         serializer = VehicleSerializer(Vehicles, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = VehicleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class vehicletDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Vehicle.objects.get(pk=pk)
#         except Vehicle.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         Vehicle = self.get_object(pk)
#         serializer = VehicleSerializer(Vehicle)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         Vehicle = self.get_object(pk)
#         serializer = VehicleSerializer(Vehicle, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         Vehicle = self.get_object(pk)
#         Vehicle.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
# #Category API
# class CategoryApiView(APIView):

#     def get(self,request):
#         Categories = Category.objects.all()
#         serializer = CategorySerializer(Categories, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CategorySerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CategoryDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Category.objects.get(pk=pk)
#         except Category.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         category = self.get_object(pk)
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         Vehicle = self.get_object(uid=pk)
#         serializer = CategorySerializer(Vehicle, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         category = self.get_object(pk)
#         category.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# #Service Api
# class ServiceApiView(APIView):

#     def get(self,request):
#         services = Service.objects.all()
#         serializer = ServiceSerializer(services, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = ServiceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ServiceDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Service.objects.get(uid=pk)
#         except Category.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         category = self.get_object(uid=pk)
#         serializer = ServiceSerializer(category)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         Service = self.get_object(uid=pk)
#         serializer = ServiceSerializer(Service, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         Service = self.get_object(uid = pk)
#         Service.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# #CarwashSale item
# class CarwashSaleItemApiView(APIView):

#     def get(self,request):
#         CarwashsaleItem = CarwashSale.objects.all()
#         serializer = CarwashSaleSerializer(CarwashsaleItem, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = CarwashSaleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class CarwashSaleItemDetail(APIView):

# #Retrieve, update or delete a snippet instance.
#     def get_object(self, pk):
#             try:
#                 return CarwashSale.objects.get(uid=pk)
#             except CarwashSale.DoesNotExist:
#                 raise Http404

#     def get(self, request, pk, format=None):
#         CarwashSaleItem = self.get_object(pk)
#         serializer = CarwashSaleSerializer(CarwashSaleItem)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         CarwashSaleItem = self.get_object(uid = pk)
#         serializer = CarwashSaleSerializer(CarwashSaleItem, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         CarwashSaleItem = self.get_object(uid = pk)
#         CarwashSaleItem.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# #Staff API
# class StaffApiView(APIView):

#     def get(self,request):
#         sale = Staff.objects.all()
#         serializer = StaffSerializer(sale, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = StaffSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class StaffDetail(APIView):

#     #Retrieve, update or delete a snippet instance.

#     def get_object(self, pk):
#         try:
#             return Staff.objects.get(uid=pk)
#         except Staff.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         staff = self.get_object(pk)
#         serializer = StaffSerializer(staff)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         staff = self.get_object(pk)
#         serializer = StaffSerializer(staff, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         staff = self.get_object(pk)
#         staff.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# """
# #Generics based API
# #CreateView, UpdateView, DeleteView, ListView, DetailView

# class CategoryList(generics.ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class VehicleList(generics.ListCreateAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer

# class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer

# class ServiceList(generics.ListCreateAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

# class ServiceDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer

# # class SaleList(generics.ListCreateAPIView):
# #     queryset = Sale.objects.all()
# #     serializer_class = SaleSerializer

# # class SaleDetail(generics.RetrieveUpdateDestroyAPIView):
# #     queryset = Sale.objects.all()
# #     serializer_class = SaleSerializer"""
