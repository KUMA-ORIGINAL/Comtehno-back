from rest_framework import serializers

from ..models import Project


class ProjectBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('title', 'slug', 'photo', 'description', 'created_at')


class ProjectSerializer(ProjectBaseSerializer):
    pass


class ProjectListSerializer(ProjectBaseSerializer):

    class Meta(ProjectBaseSerializer.Meta):
        fields = ('title', 'slug', 'description', 'full_name', 'photo', 'website_url', 'date', 'created_at',)
