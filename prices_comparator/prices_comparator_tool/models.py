from django.db import models

class ProductCategory(models.Model):
    product_name = models.CharField(verbose_name= 'Product',max_length=250)
    

class Product(models.Model):
    product_name = models.CharField( max_length=100)
    product_weight = models.FloatField(default=0)
    product_price = models.FloatField(default=0)
    total_units = models.IntegerField(default=0)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    def price_per_100g(self):
        return  self.product_price/(self.product_weight*self.total_units)*100
    
