import uuid

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from cwwms.main.models import Common

# Create your models here.

class Category(Common):
    name = models.CharField(max_length=100, unique=True)
    
    class Meta:
        ordering = ('-name',)
        verbose_name_plural = 'categories'
    
    def __str__(self) -> str:
        return self.name

class Vehicle(Common):
    category = models.ForeignKey(Category, related_name='vehicles', on_delete=models.PROTECT) 
    registration = models.CharField(max_length=10, unique=True, validators=[
            RegexValidator(
                regex='^[A-Z]{2,4}[0-9]{3,4}[A-Z]{1}$',
                message='Vehicle Registration doesn\'t comply',
            ),
        ])
    
    class Meta:
        ordering = ('-registration',)
    
    def __str__(self) -> str:
        return self.registration

class Service(Common):        
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='services', on_delete=models.PROTECT) 
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ('-name',)
        
    def __str__(self) -> str:
        return f'Created service {self.name} for category {self.category}'
    
class Sale(Common):
    class State(models.TextChoices):
        PAID = "PAID"
        UNPAID = "UNPAID"
        CANCELLED = "CANCELLED"

    vehicle = models.ForeignKey(to=Vehicle, on_delete=models.PROTECT)
    attendant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    state = models.CharField(max_length=15, choices=State.choices, default=State.PAID)
    
    class Meta:
        ordering = ('-created',)
        
    def __str__(self):
        return f'Sale #{self.id}'
 
    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost


class SaleItem(Common):
    sale = models.ForeignKey(Sale,on_delete=models.CASCADE, related_name="items")
    service = models.ForeignKey(Service, related_name='sale_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self) -> str:
        return self.uid
    
    def get_cost(self):
        return self.service.price * self.quantity


    
 
    
    