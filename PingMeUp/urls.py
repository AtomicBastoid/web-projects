from django import urls
from . import views
from django.urls import path

app_name = "PingMeUp"
urlpatterns = [
    path("pingmeup/", views.index, name="index"),
    path("pingmeup/create", views.create, name="create")
]
