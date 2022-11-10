from django.db import models
from prof.models import Profile

# Create your models here.
class Rembg(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="rembg", blank=True, null=True)
    output = models.ImageField(upload_to="rembg", blank=True, null=True)

class Ytvidmp(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    output = models.FileField(upload_to="ytvid", blank=True, null=True)

class Yt(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    output = models.FileField(upload_to="ytvid", blank=True, null=True)