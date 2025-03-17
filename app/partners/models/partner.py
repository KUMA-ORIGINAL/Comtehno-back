from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    icon = models.FileField(upload_to='partners_icons/%Y/%m/', verbose_name='Лого')
    link = models.URLField('Ссылка на партнера', blank=True, null=True)
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыт?')
    document_page = models.ForeignKey(
        'document_pages.DocumentPage', on_delete=models.SET_NULL,
        null=True, blank=True, verbose_name='Страница документов')

    class Meta:
        verbose_name = 'Партнер'
        verbose_name_plural = 'Партнеры'

    def __str__(self):
        return self.name
