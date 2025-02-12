from django.db import models
from django.utils.translation import gettext_lazy as _


class Specialty(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    specialty = models.CharField(max_length=255)
    description = models.TextField()
    preview_photo = models.FileField(upload_to='specialty/preview_photos/%Y/%m',
                                     blank=True, verbose_name=_("Превью Фото"))
    photo = models.FileField(upload_to='specialty/photos/%Y/%m',
                             blank=True, verbose_name=_("Фото"))

    category = models.ForeignKey('SpecialtyCategory', on_delete=models.CASCADE,
                                 related_name='specialty')

    def __str__(self):
        return self.title
