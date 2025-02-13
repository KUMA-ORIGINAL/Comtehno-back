from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationTabularInline

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline

from ..models import TrainingProgram, Course, Module


class ModuleInline(TabularInline, TranslationTabularInline):
    model = Module
    extra = 1


@admin.register(Course)
class CourseAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    inlines = [ModuleInline]


class CourseInline(TabularInline, TranslationTabularInline):
    model = Course
    extra = 1


@admin.register(TrainingProgram)
class TrainingProgramAdmin(UnfoldModelAdmin, TabbedTranslationAdmin):
    inlines = [CourseInline]
