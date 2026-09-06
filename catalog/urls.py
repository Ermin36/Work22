from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, products_list, product_info

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', product_info, name='product_detail'),
    path('products/', products_list, name='product_list'),
]