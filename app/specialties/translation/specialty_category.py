from modeltranslation.translator import TranslationOptions, register

from ..models import SpecialtyCategory


@register(SpecialtyCategory)
class SpecialtyCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
