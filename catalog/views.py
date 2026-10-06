from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import render
from .models import Product

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
    return render(request, 'home.html', {'cards': data})

def contacts(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')

        print([name, phone, message])

        return HttpResponse("Ваши данные получены")

    return render(request, 'contacts.html')

class ProductDetail(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

class ProductList(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

