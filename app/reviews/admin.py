from django.contrib import admin
from .models import Student, Category, Question_Answer, Review

# Кастомизация админ-панели для модели Student
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'course', 'cat', 'is_published', 'time_create', 'time_update')
    list_filter = ('is_published', 'course', 'cat')
    search_fields = ('full_name',)
    ordering = ('full_name',)

# Кастомизация админ-панели для модели Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

# Кастомизация админ-панели для модели Question_Answer
@admin.register(Question_Answer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    search_fields = ('question', 'answer')
    ordering = ('question',)

# Кастомизация админ-панели для модели Review
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('student', 'question_answer', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('student__full_name', 'question_answer__question')
    ordering = ('-created_at',)
