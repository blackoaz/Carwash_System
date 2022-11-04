from unicodedata import category
from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Service,Vehicle,CarwashSale
from users.models import CustomUser

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__' #or['field','field']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username','first_name','last_name','email','phone_number','password1','password2')


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label= 'password',widget=forms.PasswordInput)
    class Meta:
        model=CustomUser
        fields=('username','password')

    def clean(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            password=self.cleaned_data['password']

            if not authenticate(username=username,password=password):
                raise forms.ValidationError("Invalid username or Password")

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
        fields = ['vehicle','body_type','staff','service']

        # widgets = {
        #     'vehicle' : forms.TextInput(attrs={'class':'input'})
        # }