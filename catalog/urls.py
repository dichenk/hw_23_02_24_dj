from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import hello
from catalog.views import contacty
from catalog.views import ProductListView


app_name = CatalogConfig.name

urlpatterns = [
        path('', hello),
        path('contacts/', contacty),

        path('list/', ProductListView.as_view(), name='list')
        ]
