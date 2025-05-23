from modeltranslation.translator import TranslationOptions, register

from .models import Staff, StaffAchievement, StaffDepartment


@register(Staff)
class StaffTranslationOptions(TranslationOptions):
    fields = ('full_name', 'specialization', 'about_me')


@register(StaffAchievement)
class StaffAchievementTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(StaffDepartment)
class StaffDepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)