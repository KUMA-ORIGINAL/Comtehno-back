from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import ParliamentMember


@register(ParliamentMember)
class ParliamentMemberTranslationOptions(TranslationOptions):
    fields = ('full_name', 'description')
