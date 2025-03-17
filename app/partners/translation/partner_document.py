from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import PartnerDocument


@register(PartnerDocument)
class PartnerDocumentTranslationOptions(TranslationOptions):
    fields = ('title', 'subtitle')
