# from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class PostModel(models.Model):
    author = models.ForeignKey(User, default="", on_delete=models.CASCADE)
    title = models.CharField(
        verbose_name="Заголовок",
        default="",
        editable=True,
        blank=True,
        db_index=True,
        max_length=150
    )
    description = models.TextField(
        verbose_name="Описание",
        default="",
        editable=True,
        blank=True
    )
    is_moderate = models.BooleanField(default=False)
    updated = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'django_app'
        ordering = ('id',)
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'

    def __str__(self):
        return f"Post: {self.title} {self.description[:30]} [{self.pk}]"
