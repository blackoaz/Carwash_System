from dataclasses import field
from pyexpat import model
from users.models import CustomUser
from rest_framework import serializers
from rest_framework.authtoken.views import Token
from .models import Vehicle, Service, Category,Staff,CarwashSale

# ModelSerializer provides an API to create serializers
# from your models

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('uid', 'created', 'updated')

class VehicleSerializer(serializers.ModelSerializer):

    # Under class Meta, we specify our database model Todo and the fields we want to expose
    # Fields not specified here will not be exposed in the API.
    class Meta:
        model = Vehicle
        fields = '__all__'
        read_only_fields = ('uid', 'created', 'updated')

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        read_only_fields = ('uid', 'created', 'updated')

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ('uid', 'created', 'updated')

class CarwashSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarwashSale
        fields = '__all__'
        read_only_fields = ('uid', 'created', 'updated')



class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'
        read_only_fields = ('uid', 'created', 'updated')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'
        read_only_fields = ('uid', 'created', 'updated')

        extra_kwargs = {'password':{
            'write_only':True,
            'required' : True
        }}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

