from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name="タイトル")
    content = models.TextField(verbose_name="内容")
    advocate = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "advocate", verbose_name="投稿者")
    date_posted = models.DateTimeField(default=timezone.now, verbose_name="投稿日時")
    views = models.PositiveIntegerField(default=0)
    author = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        through="Comment",
        related_name = "author"
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    """コメントテーブル"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="コメント投稿者")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="投稿")
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, verbose_name="親コメント")
    content = models.TextField(verbose_name="内容")
    date_posted = models.DateTimeField(default=timezone.now, verbose_name="コメント日時")

    