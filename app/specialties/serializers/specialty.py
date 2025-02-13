from rest_framework import serializers

from .cv import CVSerializer
from .student_project import StudentProjectSerializer
from ..models import Specialty
from .specialty_category import SpecialtyCategorySerializer
from .training_program import TrainingProgramSerializer


class SpecialtyBaseSerializer(serializers.ModelSerializer):
    category = SpecialtyCategorySerializer()
    training_program = TrainingProgramSerializer()
    student_projects = StudentProjectSerializer(many=True)
    cv = CVSerializer(many=True)

    class Meta:
        model = Specialty
        fields = ('id', 'title', 'slug', 'specialty', 'description', 'photo', 'category',
                  'training_program', 'student_projects', 'cv')


class SpecialtySerializer(SpecialtyBaseSerializer):
    pass


class SpecialtyListSerializer(SpecialtyBaseSerializer):

    class Meta(SpecialtyBaseSerializer.Meta):
        fields = ('id', 'title', 'slug', 'specialty', 'preview_photo', 'category')
