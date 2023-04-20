from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user', 'Пользователь'
    MODERATOR = 'moderator', 'Модератор'
    ADMIN = 'admin', 'Администратор'


class User(AbstractUser):
    email = models.EmailField(
        'Электронная почта',
        max_length=254,
        unique=True,
    )
    username = models.CharField(
        'Имя пользователя',
        max_length=150,
        unique=True,
        validators=(UnicodeUsernameValidator(),),
    )
    role = models.CharField(
        'Роль',
        max_length=30,
        choices=UserRole.choices,
        default=UserRole.USER,
    )
    first_name = models.CharField(
        'Имя',
        max_length=20,
        blank=True,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=20,
        blank=True,
    )
    bio = models.TextField('Информация о себе', null=True, blank=True)
    confirmation_code = models.CharField(
        'Код подтверждения',
        max_length=100,
        null=True,
    )

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    @property
    def is_user(self):
        return self.role == UserRole.USER

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.username
