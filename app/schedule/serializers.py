from rest_framework import serializers
from .models import Teacher, Group, Subject, Schedule, Classroom


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'full_name']


class GroupSerializer(serializers.ModelSerializer):
    curator = TeacherSerializer()

    class Meta:
        model = Group
        fields = ['id', 'name', 'course_year', 'curator']


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'technology', 'lesson_type']


class ClassroomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classroom
        fields = ['id', 'room_number']


class ScheduleSerializer(serializers.ModelSerializer):
    subject = SubjectSerializer()
    teacher = TeacherSerializer()
    classroom = ClassroomSerializer()

    class Meta:
        model = Schedule
        fields = [
            'id',
            'group',
            'weekday',
            'lesson_number',
            'time_start',
            'time_end',
            'subject',
            'teacher',
            'classroom',
            'week_type',
        ]
