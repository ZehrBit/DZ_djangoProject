from django.db import models
from django.utils import timezone


class CustomUser(models.Model):
    username = models.CharField(max_length=150, unique=True)  # Имя пользователя, уникальное
    email = models.EmailField(unique=True)  # Электронная почта пользователя, уникальная
    password = models.CharField(max_length=150)  # Пароль пользователя

    def __str__(self):
        return self.username


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)  # Заголовок поста
    slug = models.SlugField(max_length=250)  # ЧПУ(человекопонятный URL) для поста
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)  # Автор поста, связь "один ко многим" с таблицей CustomUser
    body = models.TextField()  # Тело поста
    publish = models.DateTimeField(default=timezone.now)  # Дата и время публикации поста
    created = models.DateTimeField(auto_now_add=True)  # Дата и время создания поста
    updated = models.DateTimeField(auto_now=True)  # Дата и время последнего обновления поста
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")  # Статус поста

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post,
                             on_delete=models.CASCADE)  # Пост, к которому относится комментарий, связь "один ко многим" с таблицей Post
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)  # Пользователь, который оставил комментарий, связь "один ко многим" с таблицей CustomUser
    content = models.TextField()  # Содержание комментария
    created = models.DateTimeField(auto_now_add=True)  # Дата и время создания комментария

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'


class Project(models.Model):
    user = models.ForeignKey(CustomUser,
                             on_delete=models.CASCADE)  # Пользователь, который создал проект, связь "один ко многим" с таблицей CustomUser
    project_name = models.CharField(max_length=150)  # Название проекта
    description = models.TextField()  # Описание проекта
    created = models.DateTimeField(auto_now_add=True)  # Дата и время создания проекта

    def __str__(self):
        return self.project_name


class Version(models.Model):
    project = models.ForeignKey(Project,
                                on_delete=models.CASCADE)  # Проект, к которому относится версия, связь "один ко многим" с таблицей Project
    version_number = models.CharField(max_length=50)  # Номер версии
    changes = models.TextField()  # Описание изменений в версии

    def __str__(self):
        return f'{self.project.project_name} - {self.version_number}'

