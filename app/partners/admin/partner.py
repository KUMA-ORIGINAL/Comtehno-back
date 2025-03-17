from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.decorators import display

from ..models import Partner


@admin.register(Partner)
class PartnerAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name', 'is_hidden', 'display_icon')
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_editable = ('is_hidden',)

    @display(description=_("Фото"))
    def display_icon(self, obj):
        if obj.icon:
            return mark_safe(
                f'<img src="{obj.icon.url}" width="100" '
                f'style="border-radius: 10px;" />')
