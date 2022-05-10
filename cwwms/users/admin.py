from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import CustomUser
        
admin.site.register(CustomUser)