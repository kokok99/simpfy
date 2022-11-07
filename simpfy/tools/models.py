from django.db import models

# Create your models here.
class Rembg(models.Model):
    image = models.ImageField(upload_to="RemBg", blank=True, null=True)
    output = models.ImageField(upload_to="RemBg", blank=True, null=True)