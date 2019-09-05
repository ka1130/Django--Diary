from django.urls import path
from .views import (
    PostsListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
)

urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
]
