from django.db import models
from django.utils.translation import gettext_lazy as _

from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class SpecialtyCategory(models.Model):
    name = models.CharField(max_length=255)
    photo = ProcessedImageField(upload_to='specialty/photos/%Y/%m',
                                processors=[ResizeToFill(25, 25)],
                                format='JPEG',
                                options={'quality': 80},
                                blank=True, verbose_name=_("Фото"))

    def __str__(self):
        return self.name
