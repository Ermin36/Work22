from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import (home, contacts, ProductList,
                           ProductDetail, ProductCreate, ProductUpdate, ProductDelete, ProductCategoryView)

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products/<int:pk>/', cache_page(60*15)(ProductDetail.as_view()), name='product_detail'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('products/create/', ProductCreate.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdate.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDelete.as_view(), name='product_delete'),
    path('products/category/<int:pk>/', ProductCategoryView.as_view(), name='product_category'),
]