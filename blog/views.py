from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import BlogPost

# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'blog/blog_list.html'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'blog/blog_detail.html'

    def get_object(self, queryset=None):

        self.object : BlogPost = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object