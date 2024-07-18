from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path('products_comparision/<int:pk>', views.add_products_to_compare,name='add_products_to_compare'),
]