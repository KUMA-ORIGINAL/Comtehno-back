from rest_framework import mixins, viewsets

from .models import Staff
from .serializers import StaffSerializer


class StaffViewSet(viewsets.GenericViewSet,
                   mixins.ListModelMixin):
    serializer_class = StaffSerializer
    queryset = Staff.objects.all()
