from rest_framework import serializers

from ..models import PartnerDocumentItem


class PartnerDocumentItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartnerDocumentItem
        fields = ('id', 'name', 'document')
