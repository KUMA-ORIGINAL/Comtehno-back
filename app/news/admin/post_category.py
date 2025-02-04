from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin

from news.models import PostCategory


@admin.register(PostCategory)
class PostCategoryAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name',)
