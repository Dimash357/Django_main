# Generated by Django 4.1.7 on 2023-02-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0005_rename_user_postcomment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='User',
            new_name='user',
        ),
    ]
