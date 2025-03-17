from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, mixins

from ..models import Partner
from ..serializers import PartnerSerializer


@extend_schema(tags=['Partner'])
class PartnerViewSet(viewsets.GenericViewSet,
                     mixins.ListModelMixin,):
    serializer_class = PartnerSerializer
    queryset = Partner.objects.filter(is_hidden=False)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('document_page',)
