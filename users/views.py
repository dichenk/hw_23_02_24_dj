from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import UpdateView, CreateView

from config import settings
from users.forms import CustomUserCreationForm, CustomEditUserForm
from users.models import User
from users.tokens import account_activation_token


class CustomLoginView(LoginView):
    model = User
    template_name = 'users/login.html'
    success_url = reverse_lazy('catalog:home')


class UserCreateProfileView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/create.html'

    def form_valid(self, form):
        if form.is_valid():
            self.object = form.save()
            activate_email(self.object)
        return super().form_valid(form)


def activate_email(new_user):
    print(new_user.pk)
    new_user.is_active = False
    mail_subject = 'Activate your user account.'
    message = render_to_string('users/template_activate_account.html', {
        'user': new_user.username,
        'domain': settings.BASE_URL,
        'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
        'token': account_activation_token.make_token(new_user),
        'protocol': 'http'
    })
    email = EmailMessage(mail_subject, message, to=[new_user.email])
    email.send()


def activate(request, uidb64, token):
    Userr = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Userr.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Userr.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('users:login')
    return redirect('catalog:home')


class UserEditProfileView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'users/profile.html'
    form_class = CustomEditUserForm
    success_url = reverse_lazy('catalog:home')

    def get_object(self, queryset=None):
        return self.request.user
