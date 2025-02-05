from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import Event


@register(Event)
class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
