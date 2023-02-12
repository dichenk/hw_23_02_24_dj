from django import forms

from catalog.models import Product, Category, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'


    def clean_name(self):
        name = self.cleaned_data['name']
        avoid = [
            'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно',
            'обман', 'полиция', 'радар'
        ]

        if name in avoid:
            raise forms.ValidationError('Create better name!')
        return name

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = '__all__'

class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'
        exclude = ('sign_of_the_current_version',)

