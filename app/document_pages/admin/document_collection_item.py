from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, StackedInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline


from ..models import DocumentCollectionItem


@admin.register(DocumentCollectionItem)
class DocumentCollectionItemAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)
