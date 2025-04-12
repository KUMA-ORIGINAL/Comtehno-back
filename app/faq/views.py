from django.shortcuts import render
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema

from .models import FAQItem
from .serializers import FAQItemSerializer


@extend_schema(tags=['FAQ'])
class FAQItemViewSet(viewsets.ModelViewSet):
    queryset = FAQItem.objects.all()
    serializer_class = FAQItemSerializer
