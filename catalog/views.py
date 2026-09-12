from django.http import HttpResponse
from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def home(request):

    data = [
        {
            'name': 'Удобный сервис рассылок',
            'sell': 200,
            'info': ['Удобное меню', 'Доступна документация'],
        },
        {
            'name': 'Поисковик информации',
            'sell': 120,
            'info': ['Быстрый поиск', 'Качественная цена']
        }
    ]
    return render(request, 'catalog/home.html', {'cards': data})

def contacts(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print([name, phone, message])

        return HttpResponse("Ваши данные получены")

    return render(request, 'catalog/contacts.html')

def product_info(request, pk: int):
    product = Product.objects.get(pk=pk)
    product_data = {
        'name': product.name,
        'info': ['Описание: ' + product.description, 'Цена: ' + str(product.price)],
    }
    return render(request, 'catalog/product_detail.html', {'product': product_data})

def products_list(request):

    products_data = Product.objects.all()

    return render(request, 'catalog/products.html', {'products': products_data})

