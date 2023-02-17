from gettext import Catalog

from django.contrib.auth.mixins import LoginRequiredMixin
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


class ProductListView(LoginRequiredMixin, ListView):
    model = Product


class CategoryListView(LoginRequiredMixin, ListView):
    model = Category


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    extra_context = {
        'title': 'Добавление продукта'
    }


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('catalog:category_list')
    extra_context = {
        'title': 'Добавление категории'
    }


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')


class CategoryUpdateView(LoginRequiredMixin, UpdateView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('catalog:category_list')


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')


class CategoryDeleteView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('catalog:category_list')