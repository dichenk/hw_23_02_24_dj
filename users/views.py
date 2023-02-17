from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import CustomEditUserForm, CustomUserCreationForm
from users.models import User

from django_email_verification import send_email


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomRegisterForm(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
'''
    def form_valid(self, form):
  #      user = form.save()
        print('ok')
        send_email('dchenk@gmail.com')
  #      return super(CustomRegisterForm, self).form_valid(form)
'''
'''
    def form_valid(self, form):
        user = form.save()
        return_val = super(CustomRegisterForm, self).form_valid(form)
        print('ok')
        send_email(user)
        return return_val
'''
'''
    def form_valid(self, form):
        if form_valid():
            self.object = form.save()
            self.object.is_active = False
            send_register_mail()
            self.object.save()
        return super().form_valid(form)
'''


class UserEditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')


    def get_object(self, queryset=None):
        return self.request.user


