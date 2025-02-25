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
    list_display = ('id', 'student_full_name', 'student_course', 'student_category', 'created_at', 'is_published')
    list_filter = ('is_published', 'student_category', 'created_at')
    search_fields = ('student_full_name',)
    ordering = ('-created_at',)
    inlines = [QuestionAnswerInline]
