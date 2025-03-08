from rest_framework import mixins, viewsets

from .models import Staff, StaffDepartment
from .serializers import StaffSerializer, StaffDepartmentSerializer


class StaffViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()


class StaffDepartmentViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin):
    serializer_class = StaffDepartmentSerializer
    queryset = StaffDepartment.objects.all()
