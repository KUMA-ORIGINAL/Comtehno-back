from rest_framework import serializers

from specialties.models import Specialty
from specialties.serializers import SpecialtyCategorySerializer


class SpecialtyBaseSerializer(serializers.ModelSerializer):
    category = SpecialtyCategorySerializer()

    class Meta:
        model = Specialty
        fields = ('id', 'title', 'specialty', 'description', 'photo', 'category')


class SpecialtySerializer(SpecialtyBaseSerializer):
    pass


class SpecialtyListSerializer(SpecialtyBaseSerializer):

    class Meta(SpecialtyBaseSerializer.Meta):
        fields = ('id', 'title', 'specialty', 'preview_photo', 'category')
