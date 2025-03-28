# Generated by Django 5.1 on 2025-03-17 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParliamentMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('full_name_ru', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('full_name_en', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('full_name_ky', models.CharField(max_length=100, null=True, verbose_name='ФИО')),
                ('description', models.CharField(max_length=255, verbose_name='Партия')),
                ('description_ru', models.CharField(max_length=255, null=True, verbose_name='Партия')),
                ('description_en', models.CharField(max_length=255, null=True, verbose_name='Партия')),
                ('description_ky', models.CharField(max_length=255, null=True, verbose_name='Партия')),
                ('photo', models.FileField(upload_to='parliaments_members/photos/%Y/%m/%d', verbose_name='Фото')),
                ('is_hidden', models.BooleanField(default=False, verbose_name='Скрыт?')),
                ('order', models.PositiveIntegerField(default=0, verbose_name='Порядок')),
            ],
            options={
                'verbose_name': 'Член парламента',
                'verbose_name_plural': 'Члены парламента',
            },
        ),
    ]
