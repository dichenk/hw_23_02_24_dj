from django.db import models
from author.decorators import with_author  # pip install django-author - Update author and updated_by fields of
# models automatically

from tinymce.models import HTMLField

@with_author
class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование', null=True)
    info = HTMLField(blank=True, verbose_name='Описание', default="")

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}\n{self.info}\n'


def __unicode__(self):
    return u"%s" % self.your_field


@with_author
class Product(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    name = models.CharField(max_length=250, verbose_name='Наименование', default=None)
    info = HTMLField(blank=True, verbose_name='Описание', default="")
    image = models.ImageField(upload_to='products/', blank=True, verbose_name='Изображение (превью)')
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, max_length=29, null=True
    )
    price = models.CharField(max_length=250, verbose_name='Цена за покупку', null=True)
    date_create = models.DateField('Created Time', auto_now_add=True, null=True, )
    date_last_change = models.DateField('Updated Time', auto_now=True, null=True)
    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)


    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = (
            ("change_status", "can change status"),
            ("change_info", "can change info"),
            ("change_category", "can change category"),
        )

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
