# Generated by Django 4.1.7 on 2023-02-20 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_app', '0002_alter_postmodel_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
