from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from unfold.admin import ModelAdmin as UnfoldModelAdmin, StackedInline
from unfold.decorators import display

from ..models import PartnerDocument, PartnerDocumentItem


class PartnerDocumentItemInline(StackedInline, TranslationStackedInline):
    model = PartnerDocumentItem
    extra = 1


@admin.register(PartnerDocument)
class PartnerDocumentAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    compressed_fields = True
    list_display = ('id', 'title', 'is_hidden', 'order', 'display_photo')
    list_display_links = ('id', 'title',)
    list_editable = ('is_hidden',)
    search_fields = ('title',)
    list_filter = ('is_hidden',)
    inlines = (PartnerDocumentItemInline,)

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" width="100" '
                f'style="border-radius: 10px;" />')
