import uuid

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.



class Vehicle(models.Model):
    class VehicleType(models.TextChoices):
        SUV = 'SUV',
        Saloon = 'Saloon', 
        Lorry = 'Lorry',
        Bus = 'Bus',
        Motorcycle = 'Motorcyle',
        Tuktuk = 'Tuktuk',
        Tipper = 'Tipper', 
        Van = 'Van',
        Parts = 'Parts'
        
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registration = models.CharField(max_length=10, unique=True, validators=[
            RegexValidator(
                regex='^[A-Z]{2,4}[0-9]{3,4}[A-Z]{1}$',
                message='Vehicle Registration doesn\'t comply',
            ),
        ])
    vehicle_type = models.CharField(max_length=30, choices=VehicleType.choices, default='Saloon')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.registration


class Sale(models.Model):
    class State(models.TextChoices):
        PAID = "PAID"
        UNPAID = "UNPAID"
        CANCELLED = "CANCELLED"

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    vehicle = models.ForeignKey(to=Vehicle, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    attendant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    state = models.CharField(max_length=15, choices=State.choices)
    updated_at = models.DateTimeField(auto_now=True)
    
class Service(models.Model):
    class VehicleType(models.TextChoices):
        SUV = 'SUV',
        Saloon = 'Saloon', 
        Lorry = 'Lorry',
        Bus = 'Bus',
        Motorcycle = 'Motorcyle',
        Tuktuk = 'Tuktuk',
        Tipper = 'Tipper', 
        Van = 'Van',
        Parts = 'Parts'
        
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    vehicle_type = models.CharField(max_length=100, choices=VehicleType.choices)
    price = models.FloatField()

class SaleItem(models.Model):
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    sale_id = models.ForeignKey(Sale,on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    


    
 
    
    