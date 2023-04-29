from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter, SimpleRouter

from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)

comments_router = SimpleRouter()
comments_router.register('comments', CommentViewSet, basename='post-comments')

urlpatterns = [
    path('', include(router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
    path('posts/<int:post_id>/', include(comments_router.urls)),
    path('doc/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'doc/',
        SpectacularSwaggerView.as_view(url_name='api:schema'),
        name='doc',
    ),
    path(
        'redoc/',
        SpectacularRedocView.as_view(url_name='api:schema'),
        name='redoc',
    ),
]
