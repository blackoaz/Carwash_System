import email
from turtle import update
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField

class CustomUser(AbstractUser):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField()
    national_id_number = models.IntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email', 'phone_number', 'national_id_number']
    
    def __str__(self) -> str:
        return self.username