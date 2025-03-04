from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from ..models import Project


@admin.register(Project)
class ProjectAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    compressed_fields = True
    list_display = ('id', 'title', 'full_name', 'is_hidden', 'display_photo')
    list_display_links = ('id', 'title',)
    list_editable = ('is_hidden',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at', 'display_photo')

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="100" '
                f'style="border-radius: 10px;" />')
