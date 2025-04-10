from django import forms

class VideoForm(forms.Form):
    url = forms.URLField(label='YouTube URL', max_length=200)
    format = forms.ChoiceField(label='Download Format', choices=[('mp4', 'MP4'), ('mp3', 'MP3')])
    quality = forms.ChoiceField(label='Video Quality', choices=[('720p', '720p'), ('1080p', '1080p')])
    subtitles = forms.BooleanField(label='Download Subtitles', required=False)