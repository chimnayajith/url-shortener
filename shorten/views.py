from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import ShortenedUrl
from django.db.models import Q
import random
import string

def generate_code(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(request):
    if request.method == 'POST':
        original_url = request.POST['url']
        action = request.POST.get('action')

        if action == 'really_long':
            code_length = 1000
        else:
            code_length = 6

        existing_entry = ShortenedUrl.objects.filter(original_url=original_url).first()
        if existing_entry:
            if action == 'really_long':
                if not existing_entry.long_code:
                    existing_entry.long_code = generate_code(length=code_length)
                    existing_entry.save()
                short_code = existing_entry.long_code
            else:
                if not existing_entry.short_code:
                    print(code_length)
                    existing_entry.short_code = generate_code(length=code_length)
                    existing_entry.save()
                short_code = existing_entry.short_code
        else:
            short_code = generate_code(length=code_length)
            if action == 'really_long':
                ShortenedUrl.objects.create(original_url=original_url, long_code=short_code)
            else:
                ShortenedUrl.objects.create(original_url=original_url, short_code=short_code)

        full_short_url = request.build_absolute_uri('/') + short_code

        return render(request, 'result.html', {
            'short_code': short_code,
            'original_url': original_url,
            'full_short_url': full_short_url,
            'is_really_long': action == "really_long"
        })

    return render(request, 'index.html')

def redirect_url(request, code):
    try:
        url = get_object_or_404(ShortenedUrl, Q(short_code=code) | Q(long_code=code))
        return redirect(url.original_url)
    except Http404:
        return render(request, 'invalid_url.html')