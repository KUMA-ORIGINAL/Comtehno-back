from rest_framework import serializers
from .models import Category, QuestionAnswer, StudentReview


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class StudentReviewSerializer(serializers.ModelSerializer):
    student_category = CategorySerializer(read_only=True)
    question_answer = QuestionAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = StudentReview
        fields = '__all__'
