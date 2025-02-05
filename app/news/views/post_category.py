from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from ..models import PostCategory
from ..serializers import PostCategorySerializer


@extend_schema(tags=['Posts'])
class PostCategoryViewSet(viewsets.GenericViewSet,
                          mixins.ListModelMixin):
    serializer_class = PostCategorySerializer

    def get_queryset(self):
        queryset = PostCategory.objects.all()
        return queryset
