from django.contrib import admin
from catalog.models import Category, Product

#admin.site.register(Category)

#admin.site.register(Product) вместо этого:

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category',)
    search_fields = ('name', 'info',)
    list_filter = ('category', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
