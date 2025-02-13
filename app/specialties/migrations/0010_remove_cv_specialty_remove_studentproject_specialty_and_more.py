# Generated by Django 5.1 on 2025-02-13 09:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('specialties', '0009_skill_tool_cv'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='specialty',
        ),
        migrations.RemoveField(
            model_name='studentproject',
            name='specialty',
        ),
        migrations.RemoveField(
            model_name='trainingprogram',
            name='specialty',
        ),
        migrations.AddField(
            model_name='specialty',
            name='cv',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialty', to='specialties.cv'),
        ),
        migrations.AddField(
            model_name='specialty',
            name='student_projects',
            field=models.ManyToManyField(related_name='specialty', to='specialties.studentproject'),
        ),
        migrations.AddField(
            model_name='specialty',
            name='training_program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='specialty', to='specialties.trainingprogram'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='skills',
            field=models.ManyToManyField(blank=True, to='specialties.skill', verbose_name='Навыки'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='tools',
            field=models.ManyToManyField(blank=True, to='specialties.tool', verbose_name='Инструменты'),
        ),
    ]
