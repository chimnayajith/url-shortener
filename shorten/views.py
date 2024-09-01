from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import ShortenedUrl
import random
import string

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['url']
        
        existing_entry = ShortenedUrl.objects.filter(original_url=original_url).first()
        if existing_entry:
            short_code = existing_entry.short_code
        else:
            short_code = generate_short_code()
            ShortenedUrl.objects.create(original_url=original_url, short_code=short_code)
        
        return render(request, 'result.html', {'short_code': short_code})
    
    return render(request, 'index.html')

def redirect_url(request, code):
    try:
        url = get_object_or_404(ShortenedUrl, short_code=code)
        return redirect(url.original_url)
    except Http404:
        return render(request, 'invalid_url.html')

