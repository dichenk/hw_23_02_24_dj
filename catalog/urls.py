from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import hello

app_name = CatalogConfig.name

urlpatterns = [
        path('', hello)
        ]
