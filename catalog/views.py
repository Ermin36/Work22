from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.shortcuts import render

from .forms import ProductForm
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


class ProductCreate(CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')

class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

