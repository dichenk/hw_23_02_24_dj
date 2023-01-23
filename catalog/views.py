from django.shortcuts import render

def hello(request):
    return render(request, 'catalog/home.html')
