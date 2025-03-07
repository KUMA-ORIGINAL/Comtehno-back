from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django.db import models

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from .models import ApplicantPage


@admin.register(ApplicantPage)
class ApplicantPageAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": CKEditorWidget,
        }
    }
    list_display = ('name',)
