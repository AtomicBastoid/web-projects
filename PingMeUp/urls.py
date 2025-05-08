from django import urls
from . import views
from django.urls import path

app_name = "PingMeUp"
urlpatterns = [
    path("pingmeup/", views.index, name="index"),
    path("pingmeup/edit", views.edit, name="create"),

    # --------------Ajax Views----------------------
    path("ajax/profile/", views.save_profile_ajax, name="ajax_profile"),
    path("ajax/skills/", views.save_skills_ajax, name="ajax_skills"),
    path("ajax/projects/", views.save_projects_ajax, name="ajax_projects"),
    path("ajax/socials/", views.save_socials_ajax, name="ajax_socials"),

    #---------------Profile Views--------------------
    path("pingmeup/<str:username>/", views.show, name="show_profile"),

    path("test", views.test, name="test")
]
