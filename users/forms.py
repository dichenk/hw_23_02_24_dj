from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms
from django.contrib.auth import get_user_model


class CustomEditUserForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar')


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(help_text='Type you\'re email address here please', required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')


    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
