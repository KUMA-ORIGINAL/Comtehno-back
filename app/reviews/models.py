from django.db import models


class Category(models.Model):
    """
    Направление
    """
    name = models.CharField(max_length=100, verbose_name='Название направления')

    def __str__(self):
        return self.name


class QuestionAnswer(models.Model):
    
    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')


class StudentReview(models.Model):
    """
    Отзыв студента
    """
    
    student_photo = models.ImageField(upload_to='reviews/photos/%Y/%m/%d/', verbose_name='Фото студента', null=True, blank=True)
    student_full_name = models.CharField(max_length=100, verbose_name='ФИО студента')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Slug', blank=True)
    student_course = models.IntegerField(verbose_name='Курс')
    
    student_category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Направление')
    question_answer = models.ManyToManyField(QuestionAnswer, blank=True, verbose_name='Вопросы и ответы')
    
    student_status = models.CharField(
        max_length=10,
        choices=[('student', 'Студент'), ('graduate', 'Выпускник')],
        default='student',
        verbose_name='Статус студента или выпускника' 
    )
    