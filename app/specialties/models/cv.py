from django.db import models


class CV(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    photo = models.ImageField(upload_to='specialty/cv/%Y/%m', verbose_name='Аватар')
    position = models.CharField(max_length=255, verbose_name='Должность')

    tools = models.ManyToManyField('Tool', verbose_name='Инструменты', blank=True)
    skills = models.ManyToManyField('Skill', verbose_name='Навыки', blank=True)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'

    def __str__(self):
        return self.full_name


class Tool(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название инструмента')
    photo = models.FileField(upload_to='specialty/cv/tools/%Y/%m', verbose_name='Фото')

    class Meta:
        verbose_name = 'Инструмент'
        verbose_name_plural = 'Инструменты'

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название навыка')

    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'

    def __str__(self):
        return self.name[:30]
