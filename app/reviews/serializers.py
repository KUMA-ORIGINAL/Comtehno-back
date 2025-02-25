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
    question_answers = QuestionAnswerSerializer(many=True)

    class Meta:
        model = StudentReview
        fields = ['id', 'student_photo', 'student_full_name', 'slug', 'student_course', 'student_category', 'question_answers', 'created_at', 'is_published']

    def to_representation(self, instance):
        # Получаем сериализованные данные
        representation = super().to_representation(instance)
        
        # Ограничиваем количество вопрос-ответов до 3
        representation['question_answers'] = representation['question_answers'][:3]
        
        return representation



class StudentReviewDetailSerializer(serializers.ModelSerializer):
    question_answers = QuestionAnswerSerializer(many=True)
    class Meta:
        model = StudentReview
        fields = ['id', 'student_photo', 'student_full_name', 'slug', 'student_course', 'student_category',  'question_answers', 'created_at', 'is_published']


