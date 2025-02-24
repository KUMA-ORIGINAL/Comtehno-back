from django.db import models

class Student(models.Model):
    """
    Информация о студенте
    """
    photo = models.ImageField(upload_to='reviews/photos/%Y/%m/%d/', verbose_name='Фото студента', null=True, blank=True)  
    full_name = models.CharField(max_length=100, verbose_name='ФИО студента', null=False)  
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Направление')  
    course = models.IntegerField(verbose_name='Курс', null=False)  

    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')  
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления записи')  
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано или нет')  

    def __str__(self):
        return f"{self.full_name} ({self.course} курс, {self.cat})"


class Category(models.Model):
    """
    Направление
    """
    name = models.CharField(max_length=100, verbose_name='Название направления')  

    def __str__(self):
        return self.name
  

class Question_Answer(models.Model):
    """
    Вопрос-Ответ
    """
    question = models.TextField(verbose_name='Вопрос')  
    answer = models.TextField(verbose_name='Ответ')  

    def __str__(self):
        return f"Вопрос: {self.question} | Ответ: {self.answer}"


class Review(models.Model):
    """
    Отзывы студентов
    """
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='Студент')
    question_answer = models.ForeignKey(Question_Answer, on_delete=models.CASCADE, verbose_name='Вопрос-Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"Отзыв {self.student.full_name} ({self.created_at})"
