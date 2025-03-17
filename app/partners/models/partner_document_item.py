from django.db import models


class PartnerDocumentItem(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название файла')
    document = models.FileField(upload_to='partners_documents/files/%Y/%m/', verbose_name='Файл')
    partner_document = models.ForeignKey('PartnerDocument',
                                            on_delete=models.CASCADE,
                                            related_name='document_items')

    class Meta:
        verbose_name = 'Элемент коллекции Документа'
        verbose_name_plural = 'Элементы коллекции Документа'

    def __str__(self):
        return self.name
