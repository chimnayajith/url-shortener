from django.contrib import admin
from .models import ShortenedUrl

@admin.register(ShortenedUrl)
class ShortenedUrlAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'long_code', 'created_at')
    search_fields = ('original_url', 'short_code', 'long_code')
    list_filter = ('created_at',)
