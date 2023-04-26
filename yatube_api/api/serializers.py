from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'slug', 'description')
        model = Group


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = (
            'id',
            'author',
            'text',
            'pub_date',
            'image',
            'group',
        )
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
    )

    class Meta:
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='username', read_only=True)
    following = SlugRelatedField(slug_field='username', read_only=True)

    def validate(self, data: dict) -> dict:
        if (
            not isinstance(self.initial_data.get('following'), str)
            or self.initial_data['following'] == ''
        ):
            raise serializers.ValidationError('Не верное значение')
        return data

    class Meta:
        fields = ('user', 'following')
        model = Follow
