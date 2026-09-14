from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, ProductList, ProductDetail

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('products/', ProductList.as_view(), name='product_list'),
]