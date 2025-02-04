from django.db import models


class PostCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория поста'
        verbose_name_plural = 'Категории постов'

    def __str__(self):
        return self.name
