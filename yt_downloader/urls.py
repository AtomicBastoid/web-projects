from django.urls import path
from . import views

app_name = 'yt_downloader'
urlpatterns = [
    path('', views.index, name='index'),
]