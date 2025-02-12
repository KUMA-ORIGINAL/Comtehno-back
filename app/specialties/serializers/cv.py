from rest_framework import serializers
from ..models import CV, Tool, Skill


class ToolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tool
        fields = ['name', 'photo']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['name']


class CVSerializer(serializers.ModelSerializer):
    tools = ToolSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)

    class Meta:
        model = CV
        fields = ['full_name', 'photo', 'position', 'tools', 'skills']
