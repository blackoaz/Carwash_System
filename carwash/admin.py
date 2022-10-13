from django.contrib import admin


# Register your models here.
from .models import Vehicle,Category,Service,Staff,CarwashSale

class CarwashSaleAdmin(admin.ModelAdmin):
    list_display = ['vehicle','body_type','service','staff','commision']
    list_filter = ['created','staff']


admin.site.register(Vehicle)
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Staff)
admin.site.register(CarwashSale,CarwashSaleAdmin)