from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TabbedTranslationAdmin

from unfold.admin import ModelAdmin as UnfoldModelAdmin
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.decorators import display

from .models import Group, Teacher, Subject, Schedule, Classroom


@admin.register(Teacher)
class TeacherAdmin(UnfoldModelAdmin):
    list_display = ('full_name',)
    search_fields = ('full_name',)


@admin.register(Group)
class GroupAdmin(UnfoldModelAdmin):
    list_display = ('name', 'course_year', 'curator')
    list_filter = ('course_year',)
    search_fields = ('name',)
    autocomplete_fields = ['curator']


@admin.register(Subject)
class SubjectAdmin(UnfoldModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': WysiwygWidget},
    }
    list_display = ('title', 'technology', 'lesson_type')
    search_fields = ('title',)
    list_filter = ('lesson_type', 'technology')


@admin.register(Classroom)
class ClassroomAdmin(UnfoldModelAdmin):
    list_display = ('room_number',)
    search_fields = ('room_number',)


@admin.register(Schedule)
class ScheduleAdmin(UnfoldModelAdmin):
    list_display = (
        'group', 'weekday', 'lesson_number', 'subject', 'teacher',
        'classroom', 'week_type'
    )
    list_filter = ('weekday', 'week_type', 'group', 'teacher')
    search_fields = ('group__name', 'teacher__full_name', 'subject__title')
    autocomplete_fields = ['group', 'subject', 'teacher', 'classroom']
