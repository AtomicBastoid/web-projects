from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('posts/', views.posts, name='posts'),
    path('posts/create', views.create, name='create')
]