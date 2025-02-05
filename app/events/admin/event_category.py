from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin

from ..models import EventCategory


@admin.register(EventCategory)
class EventCategoryAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
