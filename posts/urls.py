from django.urls import path
from .views import (
    PostsListView,
    PostDetailView
)

urlpatterns = [
    path('', PostsListView.as_view(), name='posts-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail')
]
