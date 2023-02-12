from django import forms

from catalog.models import Product, Category, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

