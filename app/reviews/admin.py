from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from modeltranslation.admin import TabbedTranslationAdmin
from .models import Category, StudentReview, QuestionAnswer


@admin.register(Category) # Декоратор для регистрации модели в админке
class CategoryAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('id', 'name') # Поля для отображения в списке
    search_fields = ('name',) # Поля для поиска
    ordering = ('name',) # Поля для сортировки

class QuestionAnswerInline(TabularInline):
    model = QuestionAnswer # Модель, которую встраиваем
    extra = 1 # Количество полей для ввода


@admin.register(StudentReview)
class StudentReviewAdmin(ModelAdmin, TabbedTranslationAdmin):
    list_display = ('student_photo', 'student_full_name',
                    'slug', 'student_course',
                    'student_category', 'student_status',
                    'created_at', 'is_published',) # Поля для отображения в списке
    list_filter = ('is_published', 'student_category', 'created_at') # Поля для фильтрации
    search_fields = ('student_full_name',) # Поля для поиска
    ordering = ('-created_at',) # Поля для сортировки
    inlines = [QuestionAnswerInline] # Встраивание модели QuestionAnswer
