"""
This file contains Functions needed for yt_downloader project.
"""

from django.conf import settings
import os
from yt_dlp import YoutubeDL as ydl
from django.conf import settings
import re

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
    
import yt_dlp
import os

def download(url, format=None, quality=None, subtitles=None, download_path=None):
    """
    Download a video using yt-dlp with customizable options.
    
    Args:
        url (str): URL of the video to download.
        format (str): Desired format (e.g., 'mp4', 'mkv', 'mp3'). Defaults to best available.
        quality (str): Video resolution (e.g., '720p', '1080p'). Defaults to best available.
        subtitles (bool or str): Whether to download subtitles (True for default language) or specify language (e.g., 'en').
        download_path (str): Directory to save the file. Defaults to current directory.
    
    Returns:
        dict: {'title': video_title, 'path': full_download_path}
    """
    # Set up options for yt-dlp
    ydl_opts = {
        'quiet': True,  # Suppress verbose output
        'no_warnings': True,
        'outtmpl': os.path.join(download_path or '.', '%(title)s.%(ext)s'),  # Output template
    }

    # Handle format/quality
    if format == 'mp3':
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',  # Default quality for MP3
            }],
        })
    elif format:
        if quality:
            ydl_opts['format'] = f'bestvideo[height<={quality[:-1]}]+bestaudio/best[height<={quality[:-1]}]'
        else:
            ydl_opts['format'] = f'bestvideo+bestaudio/{format}'

    # Handle subtitles
    if subtitles:
        if isinstance(subtitles, str):  # Specific language
            ydl_opts['subtitleslangs'] = [subtitles]
            ydl_opts['writesubtitles'] = True
            ydl_opts['embedsubtitles'] = True
        elif subtitles is True:  # Default language
            ydl_opts['writesubtitles'] = True
            ydl_opts['subtitleslangs'] = ['en']  # Default to English
            ydl_opts['embedsubtitles'] = True

    # Download the video
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'Unknown Title')
        filename = ydl.prepare_filename(info_dict)
        full_path = os.path.abspath(filename)

    return {
        'title': video_title,
        'path': full_path
    }




full_path = os.path.join(settings.MEDIA_ROOT, 'yt_downloader')
print(full_path)
