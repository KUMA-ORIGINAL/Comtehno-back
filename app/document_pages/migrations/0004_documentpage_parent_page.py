# Generated by Django 5.1 on 2025-03-11 06:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_pages', '0003_alter_documentpage_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentpage',
            name='parent_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_pages', to='document_pages.documentpage', verbose_name='Родительская страница'),
        ),
    ]
