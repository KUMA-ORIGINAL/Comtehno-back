from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.points} points)"
