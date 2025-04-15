from modeltranslation.translator import TranslationOptions, register
from .models import QuestionAnswer, Category, StudentReview

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(QuestionAnswer)
class QuestionAnswerTranslationOptions(TranslationOptions):
    fields = ('question', 'answer')

@register(StudentReview)
class StudentReviewTranslationOptions(TranslationOptions):
    fields = ('student_full_name', )
    