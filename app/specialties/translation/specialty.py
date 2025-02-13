from modeltranslation.translator import TranslationOptions, register

from ..models import Specialty


@register(Specialty)
class SpecialtyTranslationOptions(TranslationOptions):
    fields = ('title', 'specialty', 'description')
