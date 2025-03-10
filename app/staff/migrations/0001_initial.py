# Generated by Django 5.1 on 2025-02-13 10:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, verbose_name='Полное имя')),
                ('full_name_ru', models.CharField(max_length=255, null=True, verbose_name='Полное имя')),
                ('full_name_en', models.CharField(max_length=255, null=True, verbose_name='Полное имя')),
                ('full_name_ky', models.CharField(max_length=255, null=True, verbose_name='Полное имя')),
                ('specialization', models.CharField(max_length=255, verbose_name='Специализация')),
                ('specialization_ru', models.CharField(max_length=255, null=True, verbose_name='Специализация')),
                ('specialization_en', models.CharField(max_length=255, null=True, verbose_name='Специализация')),
                ('specialization_ky', models.CharField(max_length=255, null=True, verbose_name='Специализация')),
                ('photo', models.FileField(upload_to='staff/%Y/%m/', verbose_name='Фото')),
                ('about_me', models.TextField(verbose_name='Обо мне')),
                ('about_me_ru', models.TextField(null=True, verbose_name='Обо мне')),
                ('about_me_en', models.TextField(null=True, verbose_name='Обо мне')),
                ('about_me_ky', models.TextField(null=True, verbose_name='Обо мне')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
            },
        ),
        migrations.CreateModel(
            name='StaffAchievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='achievements', to='staff.staff')),
            ],
        ),
    ]
