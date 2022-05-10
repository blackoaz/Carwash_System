from re import A
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django_tenants.admin import TenantAdminMixin

from .models import Client, CustomUser

# Register your models here.
@admin.site.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'first_name', 'last_name', 'user_type', 'is_active', 'is_staff')
    ordering = ('username'),
    
@admin.register(Client)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
        list_display = ('name', 'paid_until')