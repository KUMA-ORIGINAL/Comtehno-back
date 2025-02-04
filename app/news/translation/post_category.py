from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from news.models import PostCategory


@register(PostCategory)
class PostCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)
