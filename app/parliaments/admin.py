from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from .models import ParliamentMember


@admin.register(ParliamentMember)
class ParliamentMemberAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ("full_name", "description", 'is_hidden', 'order', "display_photo")
    search_fields = ("full_name",)
    list_editable = ('is_hidden', 'order')

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="100" '
                f'style="border-radius: 10px;" />')
