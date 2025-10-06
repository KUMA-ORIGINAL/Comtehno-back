from rest_framework import serializers
from .models import Question, Option, OptionSkill, Skill


class OptionSkillSerializer(serializers.ModelSerializer):
    skill_name = serializers.CharField(source="skill.name")

    class Meta:
        model = OptionSkill
        fields = ["skill_name", "points"]


class OptionSerializer(serializers.ModelSerializer):
    skills = serializers.SerializerMethodField()

    class Meta:
        model = Option
        fields = ["value", "text", "skills"]

    def get_skills(self, obj):
        skills = obj.option_skills.all()
        return {s.skill.name: s.points for s in skills}


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ["text", "options"]
