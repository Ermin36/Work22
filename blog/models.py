from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/image')
    date_posted = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    number_views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'blogpost'
        verbose_name_plural = 'blogposts'
        ordering = ['title']