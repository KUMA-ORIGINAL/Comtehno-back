# Generated by Django 5.1 on 2025-03-05 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_studentreview_student_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentreview',
            old_name='student_photo',
            new_name='photo',
        ),
        migrations.AlterField(
            model_name='studentreview',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано?'),
        ),
    ]
