from rest_framework import viewsets

from .models import ApplicantPage
from .serializers import ApplicantPageSerializer


class ApplicantPageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ApplicantPage.objects.all()
    serializer_class = ApplicantPageSerializer
