from rest_framework import serializers
from ..models import TrainingProgram, Course, Module


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['name']


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'modules']


class TrainingProgramSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = TrainingProgram
        fields = ['training_time', 'portfolio_projects', 'courses']
