from django.urls import path, include
from . import views

app_name = 'QRCode'
urlpatterns = [
    path('', views.index, name='index')
]