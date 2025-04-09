from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from specialties.models import Specialty


@admin.register(Specialty)
class SpecialtyAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'title', 'specialty', 'category', 'is_popular', 'display_photo')
    list_display_links = ('id', 'title',)
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('display_photo',)
    autocomplete_fields = ('student_projects',)

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="120" '
                f'style="border-radius: 10%;" />')
