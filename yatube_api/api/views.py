from django.db.models import QuerySet
from rest_framework import serializers, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, \
    IsAuthenticatedOrReadOnly

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)
from posts.models import Follow, Group, Post


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly)

    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)

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
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
