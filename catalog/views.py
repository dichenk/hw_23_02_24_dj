from django.shortcuts import render
from catalog.models import Product

def hello(request):

    context = {
        'object_list': Product.objects.all()
    }
    return render(request, 'catalog/home.html', context)
