from django.db import models


class TrainingProgram(models.Model):
    training_time = models.CharField(max_length=255, verbose_name='Время обучения')
    portfolio_projects = models.CharField(max_length=255, verbose_name='Количество работ')
    specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, null=True, blank=True,
                                  related_name='training_program')

    class Meta:
        verbose_name = 'Программа обучения'
        verbose_name_plural = 'Программы обучения'

    def __str__(self):
        return f"{self.Meta.verbose_name}: Специальность - {self.specialty}"


class Course(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    training_program = models.ForeignKey(TrainingProgram,
                                         on_delete=models.CASCADE,
                                         related_name="courses",
                                         verbose_name='Программа обучения')

    class Meta:
        verbose_name = 'Курс - Программа обучения'
        verbose_name_plural = 'Курс - Программы обучения'

    def __str__(self):
        return f'{self.name} - {self.training_program}'


class Module(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules",
                               verbose_name='Курс')

    class Meta:
        verbose_name = 'Модуль - курса'
        verbose_name_plural = 'Модуль - курса'

    def __str__(self):
        return self.name
