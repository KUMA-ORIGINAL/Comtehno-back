from django.db import models


class Staff(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='Полное имя')
    specialization = models.CharField(max_length=255, verbose_name='Специализация')
    photo = models.FileField(upload_to='staff/%Y/%m/', verbose_name='Фото')
    about_me = models.TextField(verbose_name='Обо мне')
    department = models.ForeignKey('StaffDepartment', on_delete=models.SET_NULL, verbose_name='Отделение',
                                   blank=True, null=True)

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'

    def __str__(self):
        return self.full_name


class StaffAchievement(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='achievements')


class StaffDepartment(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
