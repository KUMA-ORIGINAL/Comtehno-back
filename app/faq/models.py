from django.db import models

class FAQ(models.Model):
    """
    Модель для хранения вопросов
    """
    name = models.CharField(max_length=255, verbose_name='Вопрос')

class FAQItem(models.Model):
    """
    Модель для хранения ответов на вопросы и парсинг их с Question
    """
    question = models.ForeignKey(FAQ, on_delete=models.PROTECT, verbose_name='Вопрос-Ответ', related_name='FAQItem')
    answer = models.TextField(verbose_name='Ответ', max_length=255)

    def __str__(self):
        return f"Ответ на вопрос {self.question.name} ({self.answer})"

    @classmethod
    def create_with_question(cls, question_name, answer):
        question, created = FAQ.objects.get_or_create(name=question_name)
        return cls.objects.create(question=question, answer=answer)
