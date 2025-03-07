from django.db import models


class ApplicantPage(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Страницы абитуриентам'
        verbose_name_plural = 'Страница абитуриентам'
