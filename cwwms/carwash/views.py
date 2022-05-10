from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
from .serializer import VehicleSerializer
from .models import Vehicle


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

        