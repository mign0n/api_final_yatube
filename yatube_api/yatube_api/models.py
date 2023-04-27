from behaviors.behaviors import Timestamped
from django.contrib.auth import get_user_model
from django.db import models

from yatube_api.utils import cut_text

User = get_user_model()

PREVIEW_LENGTH = 15


class AuthorBaseModel(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='автор',
        help_text='Автор',
    )

    class Meta:
        abstract = True


class TimeStampedModel(AuthorBaseModel, Timestamped):
    class Meta:
        abstract = True


class TextBaseModel(TimeStampedModel):
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата публикации',
    )
    text = models.TextField(
        verbose_name='текст',
        help_text='Введите текст',
    )

    class Meta:
        abstract = True
        ordering = ('pub_date',)
        default_related_name = '%(class)s'

    def __str__(self) -> str:
        return cut_text(self.text, PREVIEW_LENGTH)
