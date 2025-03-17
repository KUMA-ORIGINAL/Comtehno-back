from django.db import models


class PartnerDocument(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=255, verbose_name='Под заголовок')
    photo = models.FileField(verbose_name="Фото", upload_to="partner_documents/photos/%Y/%m/")
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыт?')
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Коллекция документов"
        verbose_name_plural = "Коллекции документов"
        ordering = ('order',)

    def __str__(self):
        return self.title
