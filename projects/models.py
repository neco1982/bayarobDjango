#from tinymce import HTMLField
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from embed_video.fields import EmbedVideoField



User = get_user_model()



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):    
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    overview = models.CharField(max_length=300)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)    
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    video_link = EmbedVideoField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField()
    #previous_page = models.ForeignKey('self', related_name='previous', on_delete=models.SET_NULL, blank=True, null=True)
    #next_page = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', kwargs={
            'slug': self.slug
        })

    # @property
    # def get_comments(self):#related name
    #      return self.comments.all().order_by('-timestamp')

class Comment(models.Model):
    project = models.ForeignKey(Project, related_name= "comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)    
    content = models.TextField()
    timestamp = models.DateField(auto_now_add=True)
    #featured = models.BooleanField()

    def __str__(self):
        return '%s - %s' % (self.project.title, self.name)

