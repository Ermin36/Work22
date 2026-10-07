from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from blog.models import BlogPost

# Create your views here.
class BlogPostListView(ListView):
    model = BlogPost
    context_object_name = 'blog_posts'
    template_name = 'blog_list.html'

    def get_queryset(self):
        return BlogPost.objects.filter(is_published=True)


class BlogPostDetailView(DetailView):
    model = BlogPost
    context_object_name = 'blog_post'
    template_name = 'blog_detail.html'

    def get_object(self, queryset=None):

        self.object : BlogPost = super().get_object(queryset)
        self.object.number_views += 1
        self.object.save()
        return self.object

class BlogPostUpdateView(UpdateView):
    model = BlogPost
    context_object_name = 'blog_post'
    fields = ('title', 'content')
    template_name = 'blog_update.html'
    success_url = reverse_lazy('blog:blog_list')

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])