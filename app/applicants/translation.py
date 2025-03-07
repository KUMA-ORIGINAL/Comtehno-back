from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from .models import ApplicantPage


@register(ApplicantPage)
class ApplicantPageTranslationOptions(TranslationOptions):
    fields = ('name', 'text')
