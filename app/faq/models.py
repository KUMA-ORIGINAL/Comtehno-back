from django.db import models

class FAQ(models.Model):

    name = models.TextField(max_length=255, verbose_name='Место')

    
    def __str__(self):
        return self.name


class FAQItem(models.Model):

    location = models.ForeignKey(FAQ, on_delete=models.PROTECT, verbose_name='Место')
    question = models.TextField(verbose_name='Вопрос', max_length=255)
    answer = models.TextField(verbose_name='Ответ', max_length=255)

    def __str__(self):
        return {self.location}, {self.question}, {self.answer}
