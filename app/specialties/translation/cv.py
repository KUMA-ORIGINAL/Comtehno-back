from modeltranslation.translator import TranslationOptions, register

from ..models import CV, Tool, Skill


@register(CV)
class CVTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position')


@register(Tool)
class ToolTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Skill)
class SkillTranslationOptions(TranslationOptions):
    fields = ('name',)
