from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline

from ..models import TrainingProgram, Course, Module


class ModuleInline(TabularInline):
    model = Module
    extra = 1


@admin.register(Course)
class CourseAdmin(UnfoldModelAdmin):
    inlines = [ModuleInline]


class CourseInline(TabularInline):
    model = Course
    extra = 1


@admin.register(TrainingProgram)
class TrainingProgramAdmin(UnfoldModelAdmin):
    inlines = [CourseInline]
