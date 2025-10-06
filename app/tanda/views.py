from rest_framework import generics
from drf_spectacular.utils import extend_schema
from .models import Question
from .serializers import QuestionSerializer


@extend_schema(tags=['Tanda'])
class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.prefetch_related("options__option_skills__skill")
    serializer_class = QuestionSerializer
