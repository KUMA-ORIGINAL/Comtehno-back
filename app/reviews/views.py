from rest_framework import generics
from .models import Student, Review
from .serializers import StudentSerializer, ReviewSerializer
from drf_spectacular.utils import extend_schema

# API для получения списка студентов
@extend_schema(tags=['Reviews'])
class StudentListAPIView(generics.ListAPIView):
    queryset = Student.objects.filter(is_published=True)  # Фильтруем только опубликованные
    serializer_class = StudentSerializer

# API для получения списка отзывов
@extend_schema(tags=['Reviews'])
class ReviewListAPIView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

