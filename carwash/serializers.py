from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import Vehicle, Service, Category

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
        
