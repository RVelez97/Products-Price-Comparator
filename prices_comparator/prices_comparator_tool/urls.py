from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("delete/<int:pk>", views.delete_product_category, name="delete_product_category"),
    path('products_comparision/<int:pk>', views.add_products_to_compare,name='add_products_to_compare'),
    path('delete/<int:pk>', views.delete_product,name='delete_product')
]