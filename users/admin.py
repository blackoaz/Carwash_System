from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from .models import CustomUser


class MyCustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name','email','last_login')
    fieldsets = ()

    add_fieldsets = (
        (None,{
            'classes':('wide'),
            'fields': ('username,','first_name','last_name','email','phone_number','password1','password2')
        }),
    )
    ordering = ('username',)

admin.site.register(CustomUser,MyCustomUserAdmin)
