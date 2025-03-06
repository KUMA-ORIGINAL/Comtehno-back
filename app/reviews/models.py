from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    """
    Направление
    """
    name = models.CharField(max_length=100, verbose_name='Название направления')

    def __str__(self):
        return self.name
    

class StudentReview(models.Model):
    """
    Объединенная модель, содержащая информацию о студенте
    """
    # Поля, связанные со студентом
    student_photo = models.ImageField(upload_to='reviews/photos/%Y/%m/%d/', verbose_name='Фото студента', null=True, blank=True)
    student_full_name = models.CharField(max_length=100, verbose_name='ФИО студента')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug', blank=True)
    student_course = models.IntegerField(verbose_name='Курс')
    student_category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Направление')
    
    student_status = models.CharField(
        max_length=10,
        choices=[('student', 'Студент'), ('graduate', 'Выпускник')],
        default='student',
        verbose_name='Статус студента или выпускника' 
    )
    

    # Поля, связанные с отзывами
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    # Поля для управления публикацией и временем обновления
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано или нет')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.student_full_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Отзыв {self.student_full_name} ({self.created_at})"


class QuestionAnswer(models.Model):
    
    
    student_review = models.ForeignKey(StudentReview, on_delete=models.PROTECT, verbose_name='Студент', related_name='question_answers')
    
    # Поля, связанные с вопросами и ответами
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')
