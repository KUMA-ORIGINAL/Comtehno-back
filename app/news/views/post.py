from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from news.models import Post
from news.serializers import PostListSerializer, PostSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(is_hidden=True)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category',)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return PostSerializer
