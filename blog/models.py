from django.db import models
from django.urls import reverse

class The_best_blog(models.Model):
    STATUSES = (
        ('1', 'опубликован'),
        ('0', 'не опубликован')
    )



    header = models.CharField(max_length=250, verbose_name='Заголовок', default=None)
    slug = models.SlugField(null=True)
    content = models.TextField(verbose_name='Содержимое', null=True)
    preview = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name='Изображение (превью)')
    date_of_creation = models.DateField('Created Time', auto_now_add=True, null=True,)
    sign_of_publication = models.CharField(choices=STATUSES, default='0', max_length=20)
    numbers_of_views = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'

    def __str__(self):
        return self.header

#    def get_absolute_url(self):
 #       return reverse('the_best_blog_detail', )

