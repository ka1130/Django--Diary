from django.urls import path
from .views import (
    PostsListView,
    PostDetailView,
    PostCreateView,
)

urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view, name='post-create'),
]
