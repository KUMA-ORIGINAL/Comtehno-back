from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from modeltranslation.admin import TabbedTranslationAdmin
from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from ..models import CV, Tool, Skill


@admin.register(CV)
class CVAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('full_name', 'position', 'display_photo')
    search_fields = ('full_name',)
    list_filter = ('specialty',)
    filter_horizontal = ('tools', 'skills')
    readonly_fields = ('display_photo',)

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="120" '
                f'style="border-radius: 10%;" />')


@admin.register(Tool)
class ToolAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('name', 'display_photo')
    search_fields = ('name',)
    readonly_fields = ('display_photo',)

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="120" '
                f'style="border-radius: 10%;" />')


@admin.register(Skill)
class SkillAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('name',)

