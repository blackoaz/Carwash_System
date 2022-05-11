from rest_framework import generics, serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .serializer import SaleSerializer, SaleItemSerializer, ServiceSerializer, VehicleSerializer
from .models import Sale, SaleItem, Service, Vehicle


@api_view(['POST'])
def create_vehicle(request):
    vehicle = VehicleSerializer(data=request.data)
    
    if Vehicle.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This vehicle already exists')
    
    if vehicle.is_valid():
        vehicle.save()
        return Response(vehicle.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class VehicleList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class ServiceList(generics.ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
     
        
        