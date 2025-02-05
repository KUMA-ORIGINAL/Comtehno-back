from django.db import models


class Event(models.Model):
    title = models.CharField(verbose_name="Название", max_length=250)
    slug = models.SlugField(verbose_name="Ссылка", unique=True)
    content = models.TextField(verbose_name="Контент")
    place = models.CharField(verbose_name="Место проведения", max_length=255)

    photo = models.FileField(verbose_name="Фото", upload_to="events/photos/%Y/%m/%d")
    category = models.ForeignKey('EventCategory', on_delete=models.CASCADE,
                                 related_name='posts', verbose_name='Категория')
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыт?')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        ordering = ('-created_at',)
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

    def __str__(self):
        return self.title
