from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
def posts(request):
    posts = Post.objects.all()

    return render(request, 'blog/posts.html', {
        'posts': posts
    })

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/posts")
    else:
        form = PostForm()

    return render(request, 'blog/create.html', {"form": form})

