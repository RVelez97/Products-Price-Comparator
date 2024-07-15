import django_tables2 as tables
from .models import ProductCategory

class ProductTable(tables.Table):
    class Meta:
        model = ProductCategory
        fields = ('product_name',)