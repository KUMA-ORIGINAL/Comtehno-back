from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import Category, StudentReview, QuestionAnswer


@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)


class QuestionAnswerInline(TabularInline):
    model = QuestionAnswer
    extra = 1


@admin.register(StudentReview)
class StudentReviewAdmin(ModelAdmin):
    list_display = ('id', 'full_name', 'course', 'category', 'created_at', 'is_published')
    list_display_links = ('id', 'full_name')
    list_filter = ('is_published', 'category', 'created_at')
    list_editable = ('is_published',)
    search_fields = ('full_name',)
    ordering = ('-created_at',)
    inlines = [QuestionAnswerInline]
