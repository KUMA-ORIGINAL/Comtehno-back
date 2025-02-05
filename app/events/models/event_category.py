from django.db import models


class EventCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'Категория мероприятия'
        verbose_name_plural = 'Категории мероприятия'

    def __str__(self):
        return self.name
