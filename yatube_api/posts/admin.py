from django.contrib import admin

from posts import models
from yatube_api.admin import BaseAdmin


@admin.register(models.Comment)
class CommentAdmin(BaseAdmin):
    list_display = (
        'post',
        'author',
        'text',
    )
    search_fields = ('text',)
    list_filter = (
        'author',
        'pub_date',
    )


@admin.register(models.Follow)
class FollowAdmin(BaseAdmin):
    list_display = ('following', 'user', '__str__')
    list_filter = ('following', 'user')
    search_fields = ('following', 'user')


@admin.register(models.Group)
class GroupAdmin(BaseAdmin):
    list_display = (
        'pk',
        'title',
        'description',
        'slug',
        '__str__',
    )
    search_fields = ('title',)


@admin.register(models.Post)
class PostAdmin(BaseAdmin):
    list_display = (
        'pk',
        'text',
        'pub_date',
        'author',
        'group',
        'image',
        '__str__',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)
    list_editable = (
        'group',
        'image',
    )
