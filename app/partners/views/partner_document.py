from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from ..models import PartnerDocument
from ..serializers import PartnerDocumentSerializer


@extend_schema(tags=['Partner'])
class PartnerDocumentViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin,):
    serializer_class = PartnerDocumentSerializer

    def get_queryset(self):
        queryset = PartnerDocument.objects.filter(is_hidden=False)
        return queryset
