from django.db.models import Model, QuerySet
from rest_framework import filters, serializers, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Follow, Group, Post
from yatube_api.models import User


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    @property
    def get_post(self) -> QuerySet:
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self) -> QuerySet:
        return self.get_post.comments.all()

    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        serializer.save(
            author=self.request.user,
            post=self.get_post,
        )


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self) -> QuerySet:
        return Follow.objects.filter(user=self.request.user)

    @property
    def get_author(self) -> Model:
        author = self.request.data.get('following')
        if not User.objects.filter(username=author).exists():
            raise serializers.ValidationError(
                f'Объект с username={author} не существует.',
            )
        return User.objects.get(username=author)

    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        if self.get_queryset().filter(following=self.get_author).exists():
            raise serializers.ValidationError(
                'Подписка на этого пользователя уже существует.',
            )
        if self.get_author == self.request.user:
            raise serializers.ValidationError(
                'Нельзя подписаться на самого себя!',
            )
        serializer.save(following=self.get_author, user=self.request.user)
