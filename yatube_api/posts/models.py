from django.db import models

from yatube_api.models import PREVIEW_LENGTH, TextBaseModel, User
from yatube_api.utils import cut_text


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='название',
        help_text='Заголовок',
    )
    slug = models.SlugField(
        unique=True,
        verbose_name='слаг',
        help_text=(
            'Укажите адрес для страницы сообщества. Используйте только'
            ' латиницу, цифры, дефисы и знаки подчёркивания.'
        ),
    )
    description = models.TextField(
        verbose_name='описание',
        help_text='Введите краткое описание сообщества',
    )

    def __str__(self) -> str:
        return cut_text(self.title, PREVIEW_LENGTH)


class Post(TextBaseModel):
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name='сообщество',
        help_text='Сообщество для публикации поста',
    )
    image = models.ImageField(
        verbose_name='картинка',
        upload_to='posts/',
        blank=True,
        null=True,
    )

    class Meta(TextBaseModel.Meta):
        default_related_name = 'posts'


class Comment(TextBaseModel):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name='комментируемый пост',
        help_text='Текст комментируемого поста',
    )

    class Meta(TextBaseModel.Meta):
        default_related_name = 'comments'


class Follow(models.Model):
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='Автор',
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='подписчик',
        help_text='Подписчик',
    )

    class Meta:
        default_related_name = 'following'

    def __str__(self) -> str:
        return f'{self.user} подписан на {self.following}'
