from rest_framework import serializers

from document_pages.models import DocumentPage
from .document_collection import DocumentCollectionSerializer


class DocumentPageBaseSerializer(serializers.ModelSerializer):
    document_collections = DocumentCollectionSerializer(many=True, read_only=True)
    child_pages = serializers.SerializerMethodField()

    class Meta:
        model = DocumentPage
        fields = ('title', 'slug', 'subtitle', 'photo', 'content', 'child_pages','document_collections')

    def get_child_pages(self, instance):
        request = self.context.get('request')
        serializer = DocumentPageListSerializer(instance.child_pages.all(), many=True, context={'request':request})
        return serializer.data


class DocumentPageSerializer(DocumentPageBaseSerializer):
    pass


class DocumentPageListSerializer(DocumentPageBaseSerializer):

    class Meta(DocumentPageBaseSerializer.Meta):
        fields = ('title', 'slug', 'subtitle', 'photo',)
