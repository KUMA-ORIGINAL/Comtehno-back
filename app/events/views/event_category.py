from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from ..models import EventCategory
from ..serializers import EventCategorySerializer


@extend_schema(tags=['Events'])
class EventCategoryViewSet(viewsets.GenericViewSet,
                           mixins.ListModelMixin):
    serializer_class = EventCategorySerializer

    def get_queryset(self):
        queryset = EventCategory.objects.all()
        return queryset
