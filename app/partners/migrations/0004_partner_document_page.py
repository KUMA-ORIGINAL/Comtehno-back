# Generated by Django 5.1 on 2025-03-17 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document_pages', '0008_alter_documentcollection_options_and_more'),
        ('partners', '0003_partner_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='document_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='document_pages.documentpage', verbose_name='Страница документов'),
        ),
    ]
