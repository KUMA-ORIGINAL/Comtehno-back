from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, StackedInline
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline


from ..models import DocumentCollection, DocumentCollectionItem


class DocumentCollectionItemInline(StackedInline, TranslationStackedInline):
    model = DocumentCollectionItem
    extra = 1


@admin.register(DocumentCollection)
class DocumentCollectionAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = (DocumentCollectionItemInline,)
