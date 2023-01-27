from django.db import models

class The_best_blog(models.Model):
    SIGN_STATUS_ACTIVE = '1'
    SIGN_STATUS_INACTIVE = '0'
    STATUSES = (
        (SIGN_STATUS_ACTIVE, 'опубликован'),
        (SIGN_STATUS_INACTIVE, 'не опубликован')
    )



    header = models.CharField(max_length=250, verbose_name='Заголовок', default=None)
    slug = models.SlugField(null=True)
    content = models.TextField(verbose_name='Содержимое', null=True)
    preview = models.ImageField(upload_to='blog/', blank=True, null=True, verbose_name='Изображение (превью)')
    date_of_creation = models.DateField('Created Time', auto_now_add=True, null=True,)
    sign_of_publication = models.CharField(choices=STATUSES, default=SIGN_STATUS_INACTIVE, max_length=10)
    numbers_of_views = models.PositiveBigIntegerField(default=0)

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоки'

    def __str__(self):
        return self.header

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug})

The_best_blog.objects = The_best_blog.objects.using('myperfectblog')
