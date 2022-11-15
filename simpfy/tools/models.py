from django.db import models
from prof.models import Profile

# Create your models here.
class Wolf(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    quest = models.CharField(max_length=1000, null=True, blank=True)
    outputtext = models.TextField(max_length=1000, null=True, blank=True)
    outputimg = models.CharField(max_length=1000, null=True, blank=True)

class Wolfmath(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    quest = models.CharField(max_length=1000, null=True, blank=True)
    outputtext = models.TextField(max_length=1000, null=True, blank=True)
    outputimg = models.CharField(max_length=1000, null=True, blank=True)

class Wolfweather(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    quest = models.CharField(max_length=1000, null=True, blank=True)
    outputtext = models.TextField(max_length=1000, null=True, blank=True)
    outputimg = models.CharField(max_length=1000, null=True, blank=True)

class Wiki(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    quest = models.CharField(max_length=1000, null=True, blank=True)
    outputtext = models.TextField(max_length=10000, null=True, blank=True)
    
class Wikihow(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    quest = models.CharField(max_length=1000, null=True, blank=True)
    title = models.CharField(max_length=500, null=True, blank=True)
    id_title = models.CharField(max_length=100, null=True, blank=True)
    html = models.TextField(max_length=100000, null=True, blank=True)
