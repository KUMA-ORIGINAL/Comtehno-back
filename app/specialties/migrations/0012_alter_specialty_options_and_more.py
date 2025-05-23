# Generated by Django 5.1 on 2025-03-05 20:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0011_course_name_en_course_name_ky_course_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialty',
            options={'verbose_name': 'Специальность', 'verbose_name_plural': 'Специальности'},
        ),
        migrations.RemoveField(
            model_name='specialty',
            name='training_program',
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='specialty',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='specialties.specialty'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specialty', to='specialties.specialtycategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialty', to='specialties.cv', verbose_name='Резюме'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='description_en',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='description_ky',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='description_ru',
            field=models.TextField(null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Слаг'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='specialty',
            field=models.CharField(max_length=255, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='specialty_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='specialty_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='specialty_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Специальность'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='student_projects',
            field=models.ManyToManyField(related_name='specialty', to='specialties.studentproject', verbose_name='Проекты студентов'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='specialty',
            name='title_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='specialtycategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='specialtycategory',
            name='name_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='specialtycategory',
            name='name_ky',
            field=models.CharField(max_length=255, null=True, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='specialtycategory',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Название категории'),
        ),
    ]
