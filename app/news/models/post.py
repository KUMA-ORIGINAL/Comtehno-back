from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)
    content = models.TextField(verbose_name="Контент")

    photo = models.FileField(verbose_name="Фото", upload_to="news/photos/%Y/%m/%d")
    category = models.ForeignKey('PostCategory', on_delete=models.CASCADE,
                                 related_name='posts', verbose_name='Категория')
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыт?')

    created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.title
