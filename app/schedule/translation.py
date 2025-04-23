from modeltranslation.translator import register, TranslationOptions
from .models import Teacher, Group, Classroom, Subject, Schedule

@register(Teacher)
class TeacherTranslationOptions(TranslationOptions):
    fields = ('full_name',)

@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = ('name',)

@register(Classroom)
class ClassroomTranslationOptions(TranslationOptions):
    fields = ('room_number',)

@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('title', 'technology', 'lesson_type')

@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ('week_type',)