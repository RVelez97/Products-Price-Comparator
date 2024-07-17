from enum import Enum
from django.db import models


class Units(Enum):
    LONGITUDE = 'LONGITUDE'
    VOLUME = 'VOLUME'
    WEIGHT = 'WEIGHT'


class ProductCategory(models.Model):
    product_name = models.CharField(verbose_name= 'Product',max_length=250)
    measure_units = models.CharField(
        max_length=10,  
        choices=[(unit.value, unit.name) for unit in Units],
        default=Units.LONGITUDE.value
    )
    

class Product(models.Model):
    product_name = models.CharField( max_length=100)
    product_weight_volume_longitude = models.FloatField(default=0)
    product_price = models.FloatField(default=0)
    total_units = models.IntegerField(default=0)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    def price_per_measure_unit(self):
        return  self.product_price/(self.product_weight_volume_longitude*self.total_units)*100
    
