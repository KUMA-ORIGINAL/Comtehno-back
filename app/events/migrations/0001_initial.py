# Generated by Django 5.1 on 2025-02-05 17:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_en', models.CharField(max_length=255, null=True, verbose_name='Название')),
                ('name_ky', models.CharField(max_length=255, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория мероприятия',
                'verbose_name_plural': 'Категории мероприятия',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('content', models.TextField(verbose_name='Контент')),
                ('content_ru', models.TextField(null=True, verbose_name='Контент')),
                ('content_en', models.TextField(null=True, verbose_name='Контент')),
                ('content_ky', models.TextField(null=True, verbose_name='Контент')),
                ('photo', models.FileField(upload_to='events/photos/%Y/%m/%d', verbose_name='Фото')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Скрыт?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='events.eventcategory', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
                'ordering': ('-created_at',),
            },
        ),
    ]
