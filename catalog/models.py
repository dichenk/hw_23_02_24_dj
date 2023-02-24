from django.db import models

from users.models import User
from tinymce.models import HTMLField


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', null=True)
    info = models.TextField(verbose_name='Описание', null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}\n{self.info}\n'


def __unicode__(self):
    return u"%s" % self.your_field


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', default=None)
    info = HTMLField(blank=True, verbose_name='Описание', default="")
    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Изображение (превью)')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, max_length=29, null=True
    )
    price = models.CharField(max_length=250, verbose_name='Цена за покупку', null=True)
    date_create = models.DateField('Created Time', auto_now_add=True, null=True, )
    date_last_change = models.DateField('Updated Time', auto_now=True, null=True)
    author_create = models.ForeignKey(
        User, on_delete=models.CASCADE, max_length=29, null=True
    )

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}\n{self.info}\n{self.category}\n{self.price}'


class Version(models.Model):
    VERSIONS = (
        ('current version', 'текущая версия'),
        ('previous version', 'предыдущая версия'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version = models.CharField(max_length=250, verbose_name='Номер версии', default=10, blank=False)
    name_of_version = models.CharField(max_length=250, verbose_name='Название версии', default=10, blank=False)
    sign_of_the_current_version = models.CharField(choices=VERSIONS, auto_created=True, default='current version',
                                                   max_length=22)

    def __str__(self):
        return f'{self.product}\n{self.version}\n'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
