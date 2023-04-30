from django.db.models import QuerySet
from django.utils.functional import cached_property
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
from yatube_api.api.views import CreateListViewSet
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

    @cached_property
    def _post(self) -> QuerySet:
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self) -> QuerySet:
        return self._post.comments.all()

    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        serializer.save(
            author=self.request.user,
            post=self._post,
        )


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsAuthenticated, IsAuthorOrReadOnly)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self) -> QuerySet:
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer: serializers.ModelSerializer) -> None:
        serializer.save(
            following=get_object_or_404(
                User,
                username=self.request.data.get('following'),
            ),
            user=self.request.user,
        )
