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

class Qr(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    qr = models.CharField(max_length=500, null=True, blank=True)
    res = models.ImageField(upload_to='qr', null=True, blank=True)

class Bar(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='bar', null=True, blank=True)

class Hist(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='hist', null=True, blank=True)

class Line(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='line', null=True, blank=True)

class Scatter(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='scatter', null=True, blank=True)

class Line2(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='line2', null=True, blank=True)

class Xcel2csv(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='xcel', null=True, blank=True)

class Mp324(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    file = models.FileField(upload_to='mp3', null=True, blank=True)
