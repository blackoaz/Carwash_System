import django_filters
from django_filters import DateFilter
from . models import *



class CarwashSaleFilter(django_filters.FilterSet):
    start_date =  DateFilter(field_name='created',lookup_expr='gte')
    end_date =  DateFilter(field_name='created',lookup_expr='lte')
    class Meta:
        model = CarwashSale
        fields = ['service','staff','start_date','end_date']
        exclude = ['created']
