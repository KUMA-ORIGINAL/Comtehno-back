from rest_framework import serializers
from ..models import StudentProject


class StudentProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProject
        fields = ['name', 'photo']
