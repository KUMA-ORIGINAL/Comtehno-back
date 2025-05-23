from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display

from news.models import Post


@admin.register(Post)
class PostAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    compressed_fields = True
    list_display = ('id', 'title', 'category', 'is_hidden', 'display_photo')
    list_display_links = ('id', 'title',)
    list_filter = ('category',)
    list_editable = ('is_hidden',)
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('updated_at', 'display_photo')
    date_hierarchy = 'created_at'
    list_per_page = 50

    @display(description=_("Фото"))
    def display_photo(self, obj):
        if obj.photo:
            return mark_safe(
                f'<img src="{obj.photo.url}" style="border-radius: 10px; width: 170px; height: auto;" />')
