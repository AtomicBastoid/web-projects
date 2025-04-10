from django.shortcuts import render
from .forms import VideoForm
from django.conf import settings
import re
import yt_dlp
import os

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            # Process the form data and download the video
            url = form.cleaned_data['url']
            format = form.cleaned_data['format']
            quality = form.cleaned_data['quality']
            subtitles = form.cleaned_data['subtitles']

            # Logic to download the video

            # Converts URL to embed URL
            def youtube_url_to_embed(url): 
                # Match both long and short YouTube URLs
                pattern = r"(?:v=|\/)([0-9A-Za-z_-]{11})"
                match = re.search(pattern, url)

                if match:
                    video_id = match.group(1)
                    embed_url = f"https://www.youtube.com/embed/{video_id}"
                    return embed_url
                else:
                    return None
                
            # Download the video using yt-dlp
            
    else:
        form = VideoForm()

    return render(request, 'yt-downloader\index.html', {
        'form': form
        })

def success(request):
    return render(request, 'yt-downloader\success.html', {})