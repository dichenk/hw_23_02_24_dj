from django.db import transaction
from django.forms import inlineformset_factory
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView
from catalog.forms import VersionForm, ProductForm
from catalog.models import Product, Version


class ProductUpdateWithVersionView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'catalog/product_with_version.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:product_list')
        return reverse('catalog:detail_product', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        '''Использовали фабрику. В нее передали родительскую модель'''

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        print('ok')
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)


class ProductCreateWithVersionView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    template_name = 'catalog/product_form.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('catalog:product_list')
        return reverse('catalog:detail_product', args=[self.object.pk])

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)

        FormSet = inlineformset_factory(self.model, Version, form=VersionForm, extra=1)
        '''Использовали фабрику. В нее передали родительскую модель'''

        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        print('ok')
        with transaction.atomic():
            self.object = form.save()
            if formset.is_valid():
                formset.instance = self.object
                formset.save()

        return super().form_valid(form)
