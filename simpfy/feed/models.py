from django.db import models
from django.contrib.auth.models import User, auth
from prof.models import Profile
import uuid
from datetime import datetime

# Create your models here.
class Feed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images', null=True, blank=True)
    video = models.FileField(upload_to='post_videos', null=True, blank=True)
    file = models.FileField(upload_to='post_files', null=True, blank=True)
    captionvid = models.TextField(null=True, blank=True)
    captionimg = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(default=datetime.now())
    likes = models.IntegerField(default=0)
    like_stat = models.CharField(max_length=200, default="bi bi-heart")
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username

class Likes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return self.user

class Comment(models.Model):
    post = models.ForeignKey(Feed, on_delete=models.CASCADE, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True, null=True)


