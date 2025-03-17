from rest_framework import serializers

from ..models import PartnerDocument
from .partner_document_item import PartnerDocumentItemSerializer


class PartnerDocumentSerializer(serializers.ModelSerializer):
    document_items = PartnerDocumentItemSerializer(many=True, read_only=True)

    class Meta:
        model = PartnerDocument
        fields = ('id', 'title', 'subtitle', 'photo', 'document_items')
