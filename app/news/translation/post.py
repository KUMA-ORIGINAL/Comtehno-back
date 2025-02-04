from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from news.models import Post


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')
