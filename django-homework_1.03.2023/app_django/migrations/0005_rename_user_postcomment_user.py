# Generated by Django 4.1.7 on 2023-02-26 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0004_postcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='user',
            new_name='User',
        ),
    ]
