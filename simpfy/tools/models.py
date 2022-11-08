from django.db import models
from prof.models import Profile

# Create your models here.
class Rembg(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to="rembg", blank=True, null=True)
    output = models.ImageField(upload_to="rembg", blank=True, null=True)