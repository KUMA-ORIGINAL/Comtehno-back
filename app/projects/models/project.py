from django.db import models


class Project(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)
    description = models.TextField(verbose_name='Описание')
    full_name = models.CharField(verbose_name='ФИO', max_length=250)
    website_url = models.URLField(verbose_name='Ссылка на проект', blank=True)

    photo = models.FileField(verbose_name="Фото", upload_to="projects/photos/%Y/%m")
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыт?')

    date = models.DateField(verbose_name="Дата", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title
