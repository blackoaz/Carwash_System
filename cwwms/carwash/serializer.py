from rest_framework import serializers

from .models import Vehicle

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('unique_id', 'registration', 'body_type', 'created_at', 'update_at')
        