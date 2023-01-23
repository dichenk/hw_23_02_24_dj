from django.db import models

NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    info = models.TextField(verbose_name='Описание')

    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение (превью)')

    category = models.CharField(max_length=250, verbose_name='Категория')
    price = models.CharField(max_length=250, verbose_name='Цена за покупку')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_last_change = models.DateField(auto_now=True, verbose_name='Дата последнего изменения')
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


    def __str__(self):
        return f'{self.name}\n{self.info}\n{self.category}\n{self.price}'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    info = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}\n{self.info}\n'