from django.shortcuts import render
from .forms import VideoForm
from .functions import youtube_url_to_embed, download
from django.contrib.auth.decorators import login_required
from django.conf import settings
import re
import yt_dlp
import os

# Create your views here.
@login_required
def index(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            format = form.cleaned_data['format']
            quality = form.cleaned_data['quality']
            subtitles = form.cleaned_data['subtitles']

            # Convert URL to embed code
            embed_link = youtube_url_to_embed(url)

            # Download video
            download_dir = os.path.join(settings.MEDIA_ROOT, 'yt_downloader')
            download_info = download(
                url=url, 
                format=format, 
                quality=quality, 
                subtitles=subtitles, 
                download_path=download_dir
            )

            # Get relative path for URL
            full_path = download_info['path']
            # Use os.path.relpath for cross-platform compatibility
            relative_path = os.path.relpath(full_path, settings.MEDIA_ROOT)
            # Convert to URL-friendly format
            download_url = os.path.join(settings.MEDIA_URL, relative_path).replace('\\', '/')

            return render(request, 'yt-downloader/success.html', {
                "url": embed_link,
                "title": download_info['title'],
                "path": download_url  # Use the properly constructed URL
            })
    
    else:
        form = VideoForm()

    return render(request, 'yt-downloader/index.html', {
        'form': form
    })