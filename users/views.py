from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import CustomEditUserForm, CustomUserCreationForm
from users.models import User

from verify_email.email_handler import send_verification_email


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class CustomRegisterForm(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')



class UserEditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')


    def get_object(self, queryset=None):
        return self.request.user


