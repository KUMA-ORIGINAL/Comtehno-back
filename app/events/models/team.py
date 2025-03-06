from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Team(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Название команды")
    university = models.CharField(max_length=255, verbose_name="Университет")

    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.name


class Participant(models.Model):
    team = models.ForeignKey(Team, related_name='participants', on_delete=models.CASCADE, verbose_name="Команда")
    full_name = models.CharField(max_length=255, verbose_name="Полное имя")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        verbose_name="Номер телефона"
    )
    role = models.CharField(max_length=100, default='other', verbose_name="Роль")
    age = models.PositiveIntegerField(validators=[MinValueValidator(15), MaxValueValidator(100)],
                                      verbose_name="Возраст", blank=True, null=True)
    is_captain = models.BooleanField(default=False, verbose_name="Капитан команды")

    class Meta:
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

    def __str__(self):
        return f"{self.full_name} ({'Капитан' if self.is_captain else 'Участник'})"
