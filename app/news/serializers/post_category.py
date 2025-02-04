from rest_framework import serializers

from news.models import PostCategory


class PostCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = PostCategory
        fields = ('id', 'name')
