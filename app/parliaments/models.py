from django.db import models


class ParliamentMember(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    description = models.CharField(max_length=255, verbose_name="Описание")
    photo = models.FileField(verbose_name="Фото", upload_to="parliaments_members/photos/%Y/%m/%d")
    is_hidden = models.BooleanField(default=False, verbose_name='Скрыт?')
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Член парламента"
        verbose_name_plural = "Члены парламента"

    def __str__(self):
        return self.full_name
