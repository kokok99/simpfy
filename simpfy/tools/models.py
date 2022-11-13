from django.db import models
from prof.models import Profile

# Create your models here.
class Wolf(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    quest = models.CharField(max_length=1000, null=True, blank=True)
    outputtext = models.TextField(max_length=1000, null=True, blank=True)
    outputimg = models.CharField(max_length=1000, null=True, blank=True)