from django.contrib import admin

from unfold.admin import ModelAdmin as UnfoldModelAdmin, TabularInline

from ..models import Team, Participant


class ParticipantInline(TabularInline):
    model = Participant
    extra = 1  # Позволяет добавлять участников прямо из интерфейса команды
    fields = ('full_name', 'email', 'phone_number', 'role', 'age', 'is_captain')


@admin.register(Team)
class TeamAdmin(UnfoldModelAdmin):
    list_display = ('name', 'university')  # Отображение названий команд и университетов
    search_fields = ('name', 'university')  # Поля для поиска команд
    inlines = [ParticipantInline]  # Позволяет редактировать капитана и участников
    list_filter = ('university',)  # Фильтр по университету
