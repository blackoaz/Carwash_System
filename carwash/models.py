from distutils.log import info
from pyexpat.errors import messages
from time import time
from unicodedata import category
import uuid

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models

from main.models import Common

# Create your models here.
from django.db import models
import uuid

from django.conf import settings
from django.core.validators import RegexValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from main.models import Common

#Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-name',)
        verbose_name_plural = 'categories'

    def __str__(self) -> str:
        return self.name

class Vehicle(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    registration = models.CharField(max_length=10, unique=True, validators=[
            RegexValidator(
                regex='^[A-Z]{2,4}[0-9]{3,4}[A-Z]{1}$',
                message="Vehicle Registration doesn't comply",
            ),
        ])
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('-registration',)

    def __str__(self):
        return self.registration

class Service(models.Model):
    name = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)


    class Meta:
        ordering = ('-name',)

    def __str__(self) -> str:
        return f'{self.name}'

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Phone_Number = PhoneNumberField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class CarwashSale(models.Model):
    PAYMENT_STATUS = (
    ('Paid', 'Paid'),
    ('Unpaid', 'Unpaid'),
    )
    vehicle = models.CharField(max_length=10, validators=[
            RegexValidator(
                regex='^[A-Z]{2,4}[0-9]{3,4}[A-Z]{1}$',
                message="Vehicle Registration doesn't comply",
            ),
        ])
    body_type = models.CharField(max_length=100)
    #service = models.ForeignKey(Service, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    service_price = models.PositiveIntegerField(default = 0.0)
    staff = models.CharField(max_length=100)
    commision = models.PositiveIntegerField(default = 0)
    created = models.DateField(auto_now_add=True)
    time_created = models.TimeField(auto_now_add=True)
    #time = models.TimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    Payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS, default='Unpaid')
    uid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)

    class Meta:
        ordering = ('-created',)

    def save(self,*args, **kwargs):

       if self.service_price <= 99:
        self.commision = (self.service_price * 40)/100
       elif self.service_price <= 300:
        self.commision = (self.service_price * 35)/100
       else:
        self.commision = (self.service_price * 30)/100

       return super().save(*args,**kwargs)

def __str__(self):
    return self.vehicle.registration


    # category = models.ForeignKey(Category, on_delete=models.PROTECT)
    # service = models.ForeignKey(Service, on_delete=models.PROTECT)
    # staff = models.ForeignKey(Staff, on_delete=models.PROTECT)
    # commision = models.PositiveIntegerField(default = 0)
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)
    # Payment_status = models.CharField(max_length=30, choices=PAYMENT_STATUS, default='Unpaid')
    # uid = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
