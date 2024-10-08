from django.db import models

class ShortenedUrl(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=20, unique=True, null=True, blank=True)
    long_code = models.CharField(max_length=1000, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
