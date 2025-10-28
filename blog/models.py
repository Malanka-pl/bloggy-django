from django.db import models
from django.utils import timezone


"""Greeting: personal intro or short post, with optional photo and language."""
class Greeting(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    text = models.TextField()
    language = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    photo_url = models.URLField(blank=True)



