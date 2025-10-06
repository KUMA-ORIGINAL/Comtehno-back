from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline

from .models import Question, Option, Skill, OptionSkill


class OptionSkillInline(TabularInline):
    model = OptionSkill
    extra = 1


@admin.register(Option)
class OptionAdmin(ModelAdmin):
    list_display = ("text", "question")
    inlines = [OptionSkillInline]


class OptionInline(TabularInline):
    model = Option
    extra = 1
    show_change_link = True 
    fields = ("text",)      
    verbose_name = "Ответ"
    verbose_name_plural = "Ответы"


@admin.register(Question)
class QuestionAdmin(ModelAdmin):
    list_display = ("text",)


@admin.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ("name",)