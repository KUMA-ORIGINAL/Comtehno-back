from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from ..models import Event
from ..serializers import EventListSerializer, EventSerializer


@extend_schema(tags=['Events'])
class EventViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category',)
    search_fields = ('title',)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return EventSerializer

    def get_queryset(self):
        queryset = Event.objects.filter(is_hidden=False)
        return queryset
