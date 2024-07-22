from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('products_comparision/<int:pk>', views.add_products_to_compare,name='add_products_to_compare'),
    path('edit_product_category/<int:pk>',views.edit_product_category,name='edit_product_category'),
    path('edit_product/<int:pk>',views.edit_product,name='edit_product'),
]