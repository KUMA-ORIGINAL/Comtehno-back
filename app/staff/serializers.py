from rest_framework import serializers

from .models import Staff, StaffAchievement, StaffDepartment


class StaffAchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAchievement
        fields = ['name']


class StaffDepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffDepartment
        fields = ['name']


class StaffSerializer(serializers.ModelSerializer):
    achievements = StaffAchievementSerializer(many=True, read_only=True)
    department = StaffDepartmentSerializer(read_only=True)

    class Meta:
        model = Staff
        fields = ['full_name', 'specialization', 'photo', 'about_me', 'department', 'achievements']
