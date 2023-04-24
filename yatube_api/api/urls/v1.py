from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register(
    'posts/(?P<post_id>.+)/comments',
    CommentViewSet,
    basename='post-comments',
)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
