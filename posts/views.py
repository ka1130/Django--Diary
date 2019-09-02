from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Post


class PostsListView(ListView):
    model = Post
    template_name = 'posts/all_posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']
    # etc. add here
