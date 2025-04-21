from rest_framework import serializers
from .models import TrainingApplication


class TrainingApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingApplication
        fields = ('id', 'full_name', 'email', 'phone', 'comment', 'created_at')
