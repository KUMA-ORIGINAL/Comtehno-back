from django.db import models


class DocumentPage(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(unique=True)
    subtitle = models.CharField(max_length=255, verbose_name='Под заголовок')
    photo = models.FileField(verbose_name="Фото", upload_to="document_pages/photos/%Y/%m/")
    content = models.TextField(verbose_name='Контент')
    parent_page = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                    related_name='child_pages', verbose_name='Родительская страница')
    document_collections = models.ManyToManyField('DocumentCollection', blank=True,
                                                  verbose_name='Коллекции документов')
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        verbose_name = "Страница документов"
        verbose_name_plural = "Страницы документов"
        ordering = ('order',)

    def __str__(self):
        return self.title
