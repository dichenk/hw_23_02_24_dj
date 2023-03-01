from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDeleteView, \
    ProductDetailView, CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
    CreatorProductListView, ModeratorProductListView, change_publishing, startpage
from catalog.formset_views import ProductUpdateWithVersionView, ProductCreateWithVersionView

app_name = CatalogConfig.name

urlpatterns = [
    path('', startpage, name='home'),
    path('products/', ProductListView.as_view(), name='product_list'),
    path('myproducts/', CreatorProductListView.as_view(), name='my_product_list'),
    path('moderateproducts/', ModeratorProductListView.as_view(), name='moderate_product_list'),

    path('categories/', CategoryListView.as_view(), name='category_list'),

    path('create_product/', ProductCreateWithVersionView.as_view(), name='create_product'),
    path('create_category/', CategoryCreateView.as_view(), name='create_category'),

    path('update_product/<int:pk>/', ProductUpdateWithVersionView.as_view(), name='update_product'),
    path('update_category/<int:pk>/', CategoryUpdateView.as_view(), name='update_category'),

    path('delete_product/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

    path('detail_product/<int:pk>/', cache_page((ProductDetailView.as_view())), name='detail_product'),
    path('change_status/<int:pk>/', change_publishing, name='change_pub')
]
