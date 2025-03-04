from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from ..models import Project


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'full_name', 'website_url')
