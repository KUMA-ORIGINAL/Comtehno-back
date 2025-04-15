from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display

from .models import FAQItem, FAQ

@admin.register(FAQ)
class FAQAdmin(UnfoldModelAdmin):
    """
    Админка для FAQ
    """
    
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    
    list_display = ('id', 'name')
    search_fields = ('name', )
    ordering = ('name', )


@admin.register(FAQItem)
class FAQItemAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    """
    Админка для FAQItem
    """
    
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    
    list_display = ('id', 'location', 'question', 'answer') 
    search_fields = ('location', )
    ordering = ('location', )
    autocomplete_fields = ('location', )