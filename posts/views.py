from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView
)
from .models import Post


def home(request):
    # home will be replaced will sth else later
    posts = Post.objects.all()
    return render(request, 'posts/home.html', {'posts': posts})


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/all_posts.html', {'posts': posts})


class PostsListView(ListView):
    model = Post
    template_name = 'posts/all_posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
