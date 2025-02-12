from django.db import models


class StudentProject(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название проекта')
    photo = models.FileField(upload_to='specialty/student_projects/%Y/%m/',
                             verbose_name='Фото проекта')

    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE,
                                  verbose_name='Специальность', related_name='student_projects')

    class Meta:
        verbose_name = 'Проект студентов'
        verbose_name_plural = 'Проекты студентов'

    def __str__(self):
        return self.name
