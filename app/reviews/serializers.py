from rest_framework import serializers
from .models import Category, StudentReview, QuestionAnswer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionAnswer
        fields = ['question', 'answer']


class StudentReviewListSerializer(serializers.ModelSerializer):
    question_answers = QuestionAnswerSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = StudentReview
        fields = ['full_name', 'slug', 'photo', 'course', 'category',
                  'question_answers', 'created_at']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['question_answers'] = representation['question_answers'][:3]
        
        return representation


class StudentReviewDetailSerializer(serializers.ModelSerializer):
    question_answers = QuestionAnswerSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = StudentReview
        fields = ['full_name', 'slug', 'photo', 'course', 'category',
                  'question_answers', 'created_at']
