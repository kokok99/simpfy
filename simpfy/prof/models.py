from django.db import models
from django.contrib.auth.models import User
from feed.models import Feed

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    image = models.ImageField(upload_to='profile_images', default='blank.png')
    fname = models.CharField(max_length=300, null=True, blank=True)
    bio = models.CharField(max_length=300, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    saved = models.ManyToManyField(Feed, blank=True)

    def __str__(self):
        return self.user.username

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')