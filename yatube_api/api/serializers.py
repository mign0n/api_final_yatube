from django.db.models import Model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post
from yatube_api.models import User


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
    following = SlugRelatedField(
        slug_field='username',
        required=True,
        queryset=User.objects.all(),
    )

    def validate_following(self, value: str) -> str:
        user = self.context.get('request').user
        if Follow.objects.filter(
            following__exact=value,
            user__exact=user,
        ).exists():
            raise serializers.ValidationError(
                'Подписка на этого пользователя уже существует.',
            )
        if value == user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!',
            )
        return value

    def to_representation(self, instance: Model) -> dict:
        representation = super().to_representation(instance)
        representation['user'] = instance.user.username
        return representation

    class Meta:
        fields = ('user', 'following')
        model = Follow
