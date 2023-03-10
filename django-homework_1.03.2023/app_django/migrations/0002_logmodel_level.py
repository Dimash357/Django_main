# Generated by Django 4.1.7 on 2023-03-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_django', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='logmodel',
            name='level',
            field=models.CharField(choices=[('1', 'DANGER'), ('2', 'WARNING'), ('3', 'LIGHT'), ('4', 'INFO')], default='4', max_length=50),
        ),
    ]
