from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..models import Specialty
from ..serializers import SpecialtySerializer, SpecialtyListSerializer


@extend_schema(tags=['Specialties'])
class SpecialtyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Specialty.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category_id',)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return SpecialtyListSerializer
        return SpecialtySerializer
