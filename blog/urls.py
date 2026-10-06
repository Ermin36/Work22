from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogPostListView, BlogPostDetailView, BlogPostUpdateView

app_name = BlogConfig.name

urlpatterns = [
    path('blogs/', BlogPostListView.as_view(), name='blogs'),
    path('blogs/<int:pk>/detail/', BlogPostDetailView.as_view(), name='blog_detail'),
    path('blogs/<int:pk>/update/', BlogPostUpdateView.as_view(), name='blog_update'),
]