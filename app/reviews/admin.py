from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display


from .models import Category, StudentReview

@admin.register(Category)
class CategoryAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
    
    list_display = ('id', 'name') 
    search_fields = ('name',)
    
@admin.register(StudentReview)
class StudentReviewAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    
    formfield_overrides = {
        models.TextField: {
            "widget": WysiwygWidget,
        }
    }
        
    list_display = ('id', 'student_full_name', 'student_course', 'student_category') 
    search_fields = ('student_full_name',)
    ordering = ('student_category', 'student_course') # Поля для сортировки

# # #
# @admin.register(Category)
# class CategoryAdmin(UnfoldModelAdmin):
#     """
#     Админка для направления
#     """
    
#     list_display = ('id', 'name') 
#     search_fields = ('name',)        


# @admin.register(StudentReview)
# class StudentReviewAdmin(UnfoldModelAdmin):
#     """
#     Админка для отзывов студентов
#     """
    
#     formfield_overrides = {
#         models.TextField: {
#             "widget": WysiwygWidget,
#         }
#     }
    
#     list_display = ('id', 'student_full_name', 'student_course', 'student_category') 
#     search_fields = ('student_full_name',)
#     ordering = ('student_category', 'student_course')    
    