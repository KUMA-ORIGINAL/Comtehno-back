from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display

from document_pages.models import DocumentPage


@admin.register(DocumentPage)
class DocumentPageAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    list_display = ('title', 'subtitle', 'display_photo')
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('document_collections',)

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="100" '
                f'style="border-radius: 10px;" />')
