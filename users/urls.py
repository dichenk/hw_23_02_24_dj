from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.forms import CustomEditUserForm
from users.views import CustomLoginView, UserEditProfileView, CustomRegisterForm
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', UserEditProfileView.as_view(), name='profile'),
    path('register/', CustomRegisterForm.as_view(), name='register'),

]