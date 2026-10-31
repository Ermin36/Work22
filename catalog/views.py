from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .forms import ProductForm
from .models import Product, Category
from .services import get_product_in_cache


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


class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_create.html'
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        product = form.save(commit=False)
        product.owner = self.request.user
        product.is_published = True
        product.save()
        return super().form_valid(form)

class ProductDetail(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

class ProductUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'catalog.can_unpublish_product'
    model = Product
    template_name = 'product_update.html'
    form_class = ProductForm
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')

    def get_success_url(self):
        return reverse('catalog:product_detail', args=[self.kwargs.get('pk')])

class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('catalog:product_list')

class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return get_product_in_cache()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ProductCategoryView(ListView):
    model = Product
    template_name = 'product_list.html'          # можно вынести в отдельный шаблон, если нужно
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Передаём категории для выпадающего меню
        context['categories'] = Category.objects.all()

        # Опционально: передаём текущую категорию, чтобы подсветить её в меню
        current_category = Category.objects.get(pk=self.kwargs['pk'])
        context['current_category'] = current_category
        return context

