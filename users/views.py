from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import CustomEditUserForm, CustomUserCreationForm
from users.models import User


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomRegisterForm(CreateView):
    model = User
    form_class = CustomUserCreationForm

'''
    def form_valid(self, form):
        if form_valid():
            self.object = form.save()
            self.object.is_active = False
            send_register_mail()
            self.object.save()
        return super().form_valid(form)
'''


class UserEditProfileView(UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user


