# Generated by Django 5.1 on 2025-03-17 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0016_alter_course_options_course_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Курс - Программа обучения', 'verbose_name_plural': 'Курс - Программы обучения'},
        ),
        migrations.RemoveField(
            model_name='course',
            name='order',
        ),
    ]
