# Generated by Django 5.1 on 2025-02-25 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True, verbose_name='Slug'),
        ),
    ]
