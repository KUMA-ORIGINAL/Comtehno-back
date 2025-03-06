from modeltranslation.translator import TranslationOptions, register
from .models import Category, QuestionAnswer,StudentReview

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(StudentReview)
class StudentReviewTranslationOptions(TranslationOptions):
    fields = ('student_full_name', 'student_course',
              'student_status', 'student_category')
