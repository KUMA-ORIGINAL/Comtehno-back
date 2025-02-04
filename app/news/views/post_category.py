from rest_framework import viewsets, mixins

from news.models import PostCategory
from news.serializers import PostCategorySerializer


class PostCategoryViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin):
    queryset = PostCategory.objects.all()
    serializer_class = PostCategorySerializer
    lookup_field = 'slug'

