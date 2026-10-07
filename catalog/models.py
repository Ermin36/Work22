from django.db import models

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/image.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'
        ordering = ['name']