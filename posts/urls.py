from django.urls import path
from .views import (
    PostsListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register,
)

urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('register/', register, name='register'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
