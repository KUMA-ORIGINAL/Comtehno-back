from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Category, StudentReview
from .serializers import CategorySerializer, StudentReviewSerializer


# Получить список категорий
@extend_schema(tags=['Reviews'])
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


@extend_schema(tags=['Reviews'])
class StudentReviewListView(generics.ListAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewSerializer
    

@extend_schema(tags=['Reviews'])
class StudentReviewDetailView(generics.RetrieveAPIView):
    queryset = StudentReview.objects.all()
    serializer_class = StudentReviewSerializer
    lookup_field = 'slug'    
    