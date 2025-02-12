from django.db import models
from django.utils.translation import gettext_lazy as _


class SpecialtyCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = models.FileField(upload_to='specialty/photos/%Y/%m',
                             blank=True, verbose_name=_("Фото"))

    def __str__(self):
        return self.name
