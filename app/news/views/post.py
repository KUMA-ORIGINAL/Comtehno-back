from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from ..models import Post
from ..serializers import PostListSerializer, PostSerializer


@extend_schema(tags=['Posts'])
class PostViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title',)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(is_hidden=False)
        return queryset
