from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Skill
# Register your models here.

admin.site.register(Skill)
class SkillAdmin(ModelAdmin):
    list_display = ('name', 'points')
    search_fields = ('name',)

