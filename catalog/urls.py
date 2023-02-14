from django.urls import path

from config import settings
from django.conf.urls.static import static
from catalog.apps import CatalogConfig
from catalog.views import hello, ProductListView, ProductDeleteView, \
        ProductDetailView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from catalog.formset_views import ProductUpdateWithVersionView, ProductCreateWithVersionView

app_name = CatalogConfig.name

urlpatterns = [
        path('', hello, name='home'),

        path('products/', ProductListView.as_view(), name='product_list'),
        path('categories/', CategoryListView.as_view(), name='category_list'),

        path('create_product/', ProductCreateWithVersionView.as_view(), name='create_product'),
        path('create_category/', CategoryCreateView.as_view(), name='create_category'),

        path('update_product/<int:pk>/', ProductUpdateWithVersionView.as_view(), name='update_product'),
        path('update_category/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),

        path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
        path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

        path('detail_product/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
]

