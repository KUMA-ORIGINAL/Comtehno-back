from django.db import models
from django.utils.translation import gettext_lazy as _

from imagekit.models import ProcessedImageField
from pilkit.processors import ResizeToFill


class Specialty(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    specialty = models.CharField(max_length=255)
    description = models.TextField()
    preview_photo = ProcessedImageField(upload_to='specialty/preview_photos/%Y/%m',
                                        processors=[ResizeToFill(256, 256)],
                                        format='JPEG',
                                        options={'quality': 60},
                                        blank=True, verbose_name=_("Превью Фото"))
    photo = ProcessedImageField(upload_to='specialty/photos/%Y/%m',
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 80},
                                blank=True, verbose_name=_("Фото"))

    category = models.ForeignKey('SpecialtyCategory', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
