# Generated by Django 5.1 on 2025-02-05 20:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0003_course_trainingprogram_module_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс - Программа обучения', 'verbose_name_plural': 'Курс - Программы обучения'},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'verbose_name': 'Модуль - курса', 'verbose_name_plural': 'Модуль - курса'},
        ),
        migrations.AlterModelOptions(
            name='trainingprogram',
            options={'verbose_name': 'Программа обучения', 'verbose_name_plural': 'Программы обучения'},
        ),
        migrations.AddField(
            model_name='trainingprogram',
            name='specialty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='specialties.specialty', verbose_name='Специальность'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='training_program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='specialties.trainingprogram', verbose_name='Программа обучения'),
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='specialties.course', verbose_name='Курс'),
        ),
    ]
