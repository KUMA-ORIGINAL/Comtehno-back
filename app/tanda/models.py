from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Навык")

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.TextField(verbose_name="Вопрос")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text[:20]  # Показываем первые 20 символов вопроса


class Option(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        related_name="options",
        verbose_name="Вопрос"
    )
    value = models.CharField(max_length=1, verbose_name="Значение (например, A, B, C)")
    text = models.CharField(max_length=255, verbose_name="Ответ")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f"{self.text} ({self.question.text[:20]})"


class OptionSkill(models.Model):
    option = models.ForeignKey(
        Option,
        on_delete=models.CASCADE,
        related_name="option_skills",
        verbose_name="Ответ"
    )
    skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name="skill_options",
        verbose_name="Навык"
    )
    points = models.IntegerField(verbose_name="Баллы")

    class Meta:
        verbose_name = "Навык ответа"
        verbose_name_plural = "Навыки ответов"
        unique_together = ("option", "skill")

    def __str__(self):
        return f"{self.option.text} → {self.skill.name}: {self.points} баллов"
