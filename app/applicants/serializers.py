from rest_framework import serializers

from applicants.models import ApplicantPage


class ApplicantPageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApplicantPage
        fields = ('id', 'name', 'text')
