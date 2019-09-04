from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    # Usually you would put the custom form class in a forms.py file as well.
    class Meta:
        model = Post
        fields = ['title', 'content', 'created_at',
                  'category', 'tags', 'image']
        widgets = {
            'created_at': forms.DateInput(attrs={'type': 'date'}),
        }


class PostsListView(ListView):
    model = Post
    template_name = 'posts/all_posts.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # def get_form():
