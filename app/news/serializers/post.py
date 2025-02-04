from rest_framework import serializers

from news.models import Post
from news.serializers import PostCategorySerializer


class PostBaseSerializer(serializers.ModelSerializer):
    category = PostCategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('title', 'slug', 'photo', 'category', 'content', 'created_at', 'updated_at')


class PostSerializer(PostBaseSerializer):
    pass


class PostListSerializer(PostBaseSerializer):

    class Meta(PostBaseSerializer.Meta):
        fields = ('title', 'slug', 'photo', 'category', 'created_at', 'updated_at')
