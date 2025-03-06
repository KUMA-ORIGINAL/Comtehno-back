from django.db import models
from django.utils.translation import gettext_lazy as _


class Specialty(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Название"))
    slug = models.SlugField(unique=True, verbose_name=_("Слаг"))
    specialty = models.CharField(max_length=255, verbose_name=_("Специальность"))
    description = models.TextField(verbose_name=_("Описание"))
    preview_photo = models.FileField(upload_to='specialty/preview_photos/%Y/%m',
                                     blank=True, verbose_name=_("Превью Фото"))
    photo = models.FileField(upload_to='specialty/photos/%Y/%m',
                             blank=True, verbose_name=_("Фото"))
    category = models.ForeignKey('SpecialtyCategory', on_delete=models.CASCADE,
                                 related_name='specialty', verbose_name=_("Категория"))
    student_projects = models.ManyToManyField('StudentProject', related_name='specialty', verbose_name=_("Проекты студентов"))
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='specialty',
                           blank=True, null=True, verbose_name=_("Резюме"))

    class Meta:
        verbose_name = _("Специальность")
        verbose_name_plural = _("Специальности")

    def __str__(self):
        return self.title
