from gettext import Catalog

from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView


def hello(request):

    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)


class ProductListView(ListView):
    model = Product


class CategoryListView(ListView):
    model = Category


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    extra_context = {
        'title': 'Добавление продукта'
    }


class CategoryCreateView(CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('catalog:category_list')
    extra_context = {
        'title': 'Добавление категории'
    }


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class CategoryUpdateView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('catalog:category_list')


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class CategoryDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:category_list')