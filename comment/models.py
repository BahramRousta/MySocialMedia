from django.db import models
from core.models import Post


class CommentModel(models.Model):
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=100)
    body = models.CharField(max_length=500)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
