from django.shortcuts import render
from catalog.models import Product
from django.views.generic import ListView

def hello(request):

    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)

class ProductListView(ListView):
    model = Product