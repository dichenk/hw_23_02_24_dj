# Generated by Django 4.1.6 on 2023-02-24 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author_create',
            field=models.ForeignKey(max_length=29, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(max_length=29, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.category'),
        ),
    ]
