from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import EventCategory


@register(EventCategory)
class EventCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
