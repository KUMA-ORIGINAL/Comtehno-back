# Generated by Django 5.1 on 2025-03-04 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('title_ru', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_en', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('title_ky', models.CharField(max_length=250, null=True, verbose_name='Название')),
                ('slug', models.SlugField(unique=True, verbose_name='Ссылка')),
                ('description', models.TextField(verbose_name='Описание')),
                ('description_ru', models.TextField(null=True, verbose_name='Описание')),
                ('description_en', models.TextField(null=True, verbose_name='Описание')),
                ('description_ky', models.TextField(null=True, verbose_name='Описание')),
                ('full_name', models.CharField(max_length=250, verbose_name='ФИO')),
                ('full_name_ru', models.CharField(max_length=250, null=True, verbose_name='ФИO')),
                ('full_name_en', models.CharField(max_length=250, null=True, verbose_name='ФИO')),
                ('full_name_ky', models.CharField(max_length=250, null=True, verbose_name='ФИO')),
                ('website_url', models.URLField(blank=True, verbose_name='Ссылка на проект')),
                ('website_url_ru', models.URLField(blank=True, null=True, verbose_name='Ссылка на проект')),
                ('website_url_en', models.URLField(blank=True, null=True, verbose_name='Ссылка на проект')),
                ('website_url_ky', models.URLField(blank=True, null=True, verbose_name='Ссылка на проект')),
                ('photo', models.FileField(upload_to='projects/photos/%Y/%m', verbose_name='Фото')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Скрыт?')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
                'ordering': ('-created_at',),
            },
        ),
    ]
