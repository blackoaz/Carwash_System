from dataclasses import field
from pyexpat import model
from rest_framework import serializers

from .models import Vehicle, Sale, SaleItem, Service, Category

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
        
class SaleItemSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = SaleItem
        fields = ('service', 'quantity', 'uid', 'created', 'updated')
        read_only_fields = ('uid', 'created', 'updated')
        
        
class SaleSerializer(serializers.ModelSerializer):
    
    items = SaleItemSerializer(many=True)
    
    class Meta:
        model = Sale
        fields = ('uid', 'created', 'updated', 'vehicle', 'attendant', 'state', 'items')
        read_only_fields = ('uid', 'created', 'updated')
        
    # tweak create() in SaleSerializer so it can accept 
    # items alongside with the sale
    
    def create(self, validated_data):
        items = validated_data.pop("items")
        sale = Sale.objects.create(**validated_data)
        for item in items:
            SaleItem.objects.create(sale=sale, **item)
        return sale
