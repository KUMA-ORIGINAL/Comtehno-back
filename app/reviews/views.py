from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Category, StudentReview
from .serializers import CategorySerializer, StudentReviewListSerializer, StudentReviewDetailSerializer


@extend_schema(tags=['Reviews'])
class StudentReviewListView(generics.ListAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewListSerializer


@extend_schema(tags=['Reviews'])
class StudentReviewDetailView(generics.RetrieveAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewDetailSerializer
    lookup_field = 'slug'


@extend_schema(tags=['Reviews'])
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
