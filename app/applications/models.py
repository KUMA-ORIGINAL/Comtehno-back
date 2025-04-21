from django.db import models


class TrainingApplication(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    email = models.EmailField("Email")
    phone = models.CharField("Телефон", max_length=20)
    comment = models.TextField("Комментарий", blank=True)
    created_at = models.DateTimeField("Дата подачи", auto_now_add=True)
    is_processed = models.BooleanField("Обработана", default=False)

    def __str__(self):
        return f"{self.full_name}"
