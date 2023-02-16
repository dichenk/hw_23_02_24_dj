from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from users.models import User


class CustomEditUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')


class CustomUserCreationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

