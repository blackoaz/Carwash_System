import uuid

from django.db import models

# Create your models here.
BODY_CHOICES = (
    ('SUV', 'SUV'),
    ('Saloon', 'Saloon'), 
    ('Lorry', 'Lorry'),
    ('Bus', 'Bus'),
    ('Motorcycle','Motorcyle'),
    ('Tuktuk', 'Tuktuk'),
    ('Tipper', 'Tipper'), 
    ('Van', 'Van'),
    ('Vehicle parts','Vehicle Parts'),
)

class Vehicle(models.Model):
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    registration = models.CharField(max_length=10)
    body_type = models.CharField(max_length=30, choices=BODY_CHOICES, default='Saloon')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.registration