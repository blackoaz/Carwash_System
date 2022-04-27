from pyexpat import model
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'unique_id', 'is_active', 'is_staff')
    ordering = ('username'),
    
admin.site.register(CustomUser, CustomUserAdmin)