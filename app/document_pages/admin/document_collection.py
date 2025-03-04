from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline


from ..models import DocumentCollection, DocumentCollectionItem


class DocumentCollectionItemInline(TabularInline, TranslationTabularInline):
    model = DocumentCollectionItem
    extra = 1


@admin.register(DocumentCollection)
class DocumentCollectionAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('name',)
    inlines = (DocumentCollectionItemInline,)
