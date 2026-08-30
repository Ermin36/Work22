from django.core.management import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):

    help = 'Add products'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        fruits = Category.objects.create(name='Fruits', description='Свежие фрукты')
        vegetables = Category.objects.create(name='Vegetables', description='Свежие овощи')

        product_data = [
            {'name':'Яблоко', 'description':'Свежие яблоки', 'price': 12, 'category': fruits},
            {'name':'Бананы', 'description':'Свежие бананы', 'price': 17, 'category': fruits},
            {'name':'Помидоры', 'description':'Свежие помидоры', 'price': 7, 'category': vegetables},
        ]

        for data in product_data:
            product, created = Product.objects.get_or_create(**data)
            product.save()
            if created:
                self.stdout.write(self.style.SUCCESS('Product added: {}'.format(product.name)))
            else:
                self.stdout.write(self.style.SUCCESS('Product already exists: {}'.format(product.name)))