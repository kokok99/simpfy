from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime

# Create your models here.
class Feed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    video = models.FileField(upload_to='post_videos', null=True, blank=True)
    file = models.FileField(upload_to='post_files', null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    likes = models.IntegerField(default=0)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return self.user


