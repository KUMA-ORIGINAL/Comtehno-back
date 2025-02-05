from rest_framework import serializers

from ..models import Event
from .event_category import EventCategorySerializer


class EventBaseSerializer(serializers.ModelSerializer):
    category = EventCategorySerializer(read_only=True)

    class Meta:
        model = Event
        fields = ('title', 'slug', 'photo', 'place', 'category', 'content', 'created_at', 'updated_at')


class EventSerializer(EventBaseSerializer):
    pass


class EventListSerializer(EventBaseSerializer):

    class Meta(EventBaseSerializer.Meta):
        fields = ('title', 'slug', 'photo', 'place', 'category', 'created_at', 'updated_at')
