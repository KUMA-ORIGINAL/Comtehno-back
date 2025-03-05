from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline
from unfold.decorators import display

from .models import Staff, StaffAchievement, StaffDepartment


class StaffAchievementInline(TabularInline, TranslationTabularInline):
    model = StaffAchievement
    extra = 1


@admin.register(Staff)
class StaffAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('full_name', 'specialization', 'department', 'display_photo')
    search_fields = ('full_name',)
    readonly_fields = ('display_photo',)
    inlines = [StaffAchievementInline]

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="100" '
                f'style="border-radius: 10px;" />')


@admin.register(StaffDepartment)
class StaffDepartmentAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)
