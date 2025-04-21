from django.contrib import admin
from unfold.admin import ModelAdmin as UnfoldModelAdmin

from .models import TrainingApplication


@admin.register(TrainingApplication)
class TrainingApplicationAdmin(UnfoldModelAdmin):
    list_display = ('full_name', 'email', 'phone', 'is_processed', 'created_at')
    list_filter = ('is_processed', 'created_at')
    search_fields = ('full_name', 'email')
    readonly_fields = ('created_at',)
