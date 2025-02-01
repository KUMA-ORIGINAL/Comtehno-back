from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from specialties.models import SpecialtyCategory
from specialties.serializers import SpecialtyCategorySerializer


@extend_schema(tags=['Specialties Category'])
class SpecialtyCategoryViewSet(viewsets.GenericViewSet,
                               mixins.ListModelMixin):
    queryset = SpecialtyCategory.objects.all()
    serializer_class = SpecialtyCategorySerializer
