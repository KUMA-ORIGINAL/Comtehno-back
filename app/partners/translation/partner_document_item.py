from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import PartnerDocumentItem


@register(PartnerDocumentItem)
class PartnerDocumentItemTranslationOptions(TranslationOptions):
    fields = ('name', 'document')
