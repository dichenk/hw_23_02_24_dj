from django.db import models


NULLABLE = {'blank': True, 'null': True}

class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', default=None)
    info = models.TextField(verbose_name='Описание',null=True)

    image = models.ImageField(upload_to='products/', **NULLABLE, verbose_name='Изображение (превью)')

    category = models.CharField(max_length=250, verbose_name='Категория',null=True)
    price = models.CharField(max_length=250, verbose_name='Цена за покупку',null=True)
    date_create = models.DateField('Created Time', auto_now_add=True, null=True,)
    date_last_change = models.DateField('Updated Time', auto_now=True, null=True)
    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


    def __str__(self):
        return f'{self.name}\n{self.info}\n{self.category}\n{self.price}'


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование',null=True)
    info = models.TextField(verbose_name='Описание',null=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self):
        return f'{self.name}\n{self.info}\n'