from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Category, StudentReview
from .serializers import CategorySerializer, StudentReviewListSerializer, StudentReviewDetailSerializer

# Получить список отзывов
@extend_schema(tags=['Reviews'])
class StudentReviewListView(generics.ListAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewListSerializer

# Получить информацию об отзыве по slug
@extend_schema(tags=['Reviews'])
class StudentReviewDetailView(generics.RetrieveAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewDetailSerializer
    lookup_field = 'slug'

# Получить список категорий
@extend_schema(tags=['Reviews'])
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
