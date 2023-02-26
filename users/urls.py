from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import CustomLoginView, UserEditProfileView, UserCreateProfileView, activate
from users.apps import UsersConfig

app_name = UsersConfig.name


urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('register/', UserCreateProfileView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', UserEditProfileView.as_view(), name='profile'),
    path('activate/<uidb64>/<token>', activate, name='activate'),
]