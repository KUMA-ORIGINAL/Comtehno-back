from drf_spectacular.utils import extend_schema
from rest_framework import viewsets

from ..models import Project
from ..serializers import ProjectListSerializer, ProjectSerializer


@extend_schema(tags=['Projects'])
class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    search_fields = ('title',)
    lookup_field = 'slug'

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer

    def get_queryset(self):
        queryset = Project.objects.filter(is_hidden=False)
        return queryset
