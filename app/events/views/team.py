from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from ..models import Team
from ..serializers import TeamCreateSerializer


@extend_schema(tags=['Events'])
class TeamCreateViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = TeamCreateSerializer
