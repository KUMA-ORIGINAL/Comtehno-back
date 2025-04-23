from django.db import models

# Преподаватели
class Teacher(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


# Группы студентов
class Group(models.Model):
    name = models.CharField(max_length=20, unique=True)  # например, "ПИ-3-22"
    course_year = models.IntegerField()
    curator = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="curated_groups")

    def __str__(self):
        return self.name


# Аудитории
class Classroom(models.Model):
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.room_number


# Предметы (например, Web-программирование)
class Subject(models.Model):
    title = models.CharField(max_length=100)  # "Web-программирование"
    technology = models.CharField(max_length=100, blank=True)  # "Redux", "Node.js", и т.д.
    lesson_type = models.CharField(max_length=20, default="Лекция")  # Лекция / Практика / Лабораторная и т.п.

    def __str__(self):
        return f"{self.title} ({self.technology})"


# Расписание
class Schedule(models.Model):
    WEEK_TYPE_CHOICES = [
        ("Числитель", "Числитель"),
        ("Знаменатель", "Знаменатель"),
    ]

    WEEKDAYS = [
        ("Понедельник", "Понедельник"),
        ("Вторник", "Вторник"),
        ("Среда", "Среда"),
        ("Четверг", "Четверг"),
        ("Пятница", "Пятница"),
        ("Суббота", "Суббота"),
    ]

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="группы")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="преподаватели")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="предметы")
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, related_name="аудитории")

    weekday = models.CharField(max_length=15, choices=WEEKDAYS)
    time_start = models.TimeField()
    time_end = models.TimeField()
    lesson_number = models.PositiveSmallIntegerField()
    week_type = models.CharField(max_length=15, choices=WEEK_TYPE_CHOICES, default="Числитель")

    class Meta:
        ordering = ['weekday', 'lesson_number']

    def __str__(self):
        return f"{self.subject} - {self.group} ({self.weekday} {self.time_start}-{self.time_end})"

