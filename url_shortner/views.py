from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest, HttpResponseGone, JsonResponse
from .models import ShortUrl
from .utils import base62_encode
from django.core.cache import cache
from django.contrib.auth.decorators import login_required

def rate_limit(request, limit=5, window=60):
    ip = request.META.get('REMOTE_ADDR')
    key = f"rate:{ip}"

    current = cache.get(key)

    if current is None:
        cache.set(key, 1, timeout=window)
        return True
    
    if current >= limit:
        return False

    cache.incr(key)
    return True

def create_short_url(request):
    #if not rate_limit(request, limit=5):
    #    return HttpResponseBadRequest("Too many requests")

    if request.method == 'GET':
        return render(request, 'shorturl/create.html')

    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        if not long_url:
            return HttpResponseBadRequest("Url is required")

        session_token = None
        if not request.user.is_authenticated:
            if not request.session.session_key:
                request.session.create()
            session_token = request.session.session_key

        short_url = ShortUrl.objects.create(
            long_url = long_url,
            user = request.user if request.user.is_authenticated else None,
            session_token = session_token
        )

        short_key = base62_encode(short_url.id)
        short_url.short_key = short_key
        short_url.save(update_fields=['short_key'])

        short_link = request.build_absolute_uri(f"/{short_key}")

        context = {
            'short_url' : short_link,
            'long_url'  : long_url,
            'expires_at' : short_url.expires_at
        }

        return render(request, 'shorturl/create.html', context=context)
    return HttpResponseBadRequest("Post method required")


def redirect_url(request, short_key):

    #cache_key = f"short_url:{short_key}"

    #long_url = cache.get(cache_key)

    #if not long_url:
    short_url = get_object_or_404(
        ShortUrl,
        short_key=short_key,    
        is_active=True
    )
    if short_url.is_expired():
        return HttpResponseGone("Expired Link")
        
    #long_url = short_url.long_url
    #cache.set(cache_key, long_url, timeout=60*60)
    
    short_url.click_count += 1
    short_url.save(update_fields=['click_count'])

    return redirect(short_url.long_url)

@login_required
def user_url_list(request):
    urls = ShortUrl.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'user_urls': urls 
    }
    return render(request, 'shorturl/user_urls.html', context)

@login_required
def user_url_detail(request, url_id):
    url = get_object_or_404(
        ShortUrl,
        id=url_id,
        user=request.user
    )

    context = {
        'url':url
    }

    return render(request, 'shorturl/url_detail.html', context)

