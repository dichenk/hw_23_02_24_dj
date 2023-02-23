from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView

from users.forms import CustomUserCreationForm, CustomEditUserForm
from users.models import User


class CustomLoginView(LoginView):
    template_name = 'users/login.html'


class UserCreateProfileView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/create.html'


class UserEditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user
