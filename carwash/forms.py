from unicodedata import category
from django import forms
from django.forms import ModelForm
from .models import Category, Service,Vehicle,CarwashSale
from users.models import CustomUser

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__' #or['field','field']

class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','first_name','last_name','email','phone_number','national_id_number','user_type']

class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle  
        fields = ['registration','category'] 

        widgets = {
             'registration' : forms.TextInput(attrs={'class':'input','placeholder':'Enter Number Plate'})
        } 


class ServiceForm(ModelForm):
    class Meta:
        model = Service  
        fields = "__all__" 

class CarwashSaleForm(ModelForm):
    class Meta:
        model = CarwashSale  
        fields = ['vehicle','category','service','staff','Payment_status']

        # widgets = {
        #     'vehicle' : forms.TextInput(attrs={'class':'input'})
        # }            