from django.core.cache import cache
from django.db.models import QuerySet

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_product_in_cache() -> QuerySet[Product, Product]:
    if not CACHE_ENABLED:
        return Product.objects.all()
    key: str = 'products'
    products = cache.get(key)

    if products is not None:
        return products
    products = Product.objects.all()
    cache.set(key, products)
    return products


