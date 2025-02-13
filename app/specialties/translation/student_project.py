from modeltranslation.translator import TranslationOptions, register

from ..models import StudentProject


@register(StudentProject)
class StudentProjectTranslationOptions(TranslationOptions):
    fields = ('name',)
