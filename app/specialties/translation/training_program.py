from modeltranslation.translator import TranslationOptions, register

from ..models import TrainingProgram, Course, Module


@register(TrainingProgram)
class TrainingProgramTranslationOptions(TranslationOptions):
    fields = ('training_time', 'portfolio_projects')


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Module)
class ModuleTranslationOptions(TranslationOptions):
    fields = ('name',)
