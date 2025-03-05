from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название направления')

    def __str__(self):
        return self.name
    

class StudentReview(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО студента')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug', blank=True)
    photo = models.ImageField(upload_to='reviews/photos/%Y/%m', verbose_name='Фото студента',
                                      null=True, blank=True)
    course = models.IntegerField(verbose_name='Курс')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Направление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано?')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Отзыв {self.full_name} ({self.created_at})"


class QuestionAnswer(models.Model):
    student_review = models.ForeignKey(StudentReview, on_delete=models.PROTECT,
                                       verbose_name='Студент', related_name='question_answers')
    
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
