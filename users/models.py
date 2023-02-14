from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    username = models.CharField(max_length=50, verbose_name='имя пользователя', unique=True)
    email = models.EmailField(verbose_name='почта', unique=True)
    phone = models.CharField(max_length=25, verbose_name='номер телефона')
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар')
    country = models.CharField(max_length=50, verbose_name='страна')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

