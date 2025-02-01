from rest_framework import serializers

from specialties.models import SpecialtyCategory


class SpecialtyCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecialtyCategory
        fields = ('id', 'name', 'photo')
