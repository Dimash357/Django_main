# Generated by Django 4.1.7 on 2023-03-02 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_app', '0004_alter_postmodel_author_alter_postmodel_description_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('id',), 'verbose_name': 'Публикация', 'verbose_name_plural': 'Публикации'},
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='is_moderate',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(blank=True, db_index=True, default='', max_length=150, unique=True, verbose_name='Заголовок'),
        ),
    ]
