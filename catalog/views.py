from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django import template  # to check (in template) if user belongs to a group


def startpage(request):
    return render(request, 'catalog/home.html')


class ProductListView(ListView):
    model = Product
    fields = '__all__'
    template_name = 'catalog/product_list_public.html'


class CreatorProductListView(ListView, LoginRequiredMixin):  # For viewing products user's created
    model = Product
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        return Product.objects.filter(author=self.request.user)


class ModeratorProductListView(ListView):
    model = Product
    fields = '__all__'
    template_name = 'catalog/product_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status='DF')


class CategoryListView(ListView):
    model = Category


class ProductDetailView(DetailView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    fields = '__all__'


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


'''to check (in template) if user belongs to a group'''
register = template.Library()


@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


def change_publishing(request, pk):
    status_item = get_object_or_404(Product, pk=pk)
    if status_item.status == 'DF':
        status_item.status = 'PB'
    else:
        status_item.status = 'DF'
    status_item.save()
    return redirect(reverse_lazy('catalog:moderate_product_list'))
