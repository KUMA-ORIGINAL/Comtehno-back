from rest_framework import serializers
from .models import Student, Category, Question_Answer, Review

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  # Включаем все поля

class StudentSerializer(serializers.ModelSerializer):
    cat = CategorySerializer()  # Подключаем категорию (Направление)

    class Meta:
        model = Student
        fields = '__all__'

class QuestionAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question_Answer
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # Подключаем студента
    question_answer = QuestionAnswerSerializer()  # Подключаем вопрос-ответ

    class Meta:
        model = Review
        fields = '__all__'
