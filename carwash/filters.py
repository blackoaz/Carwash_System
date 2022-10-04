import django_filters
from . models import *



class CarwashSaleFilter(django_filters.FilterSet):
    class Meta:
        model = CarwashSale
        fields = ['staff','created']
