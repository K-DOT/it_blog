from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError
from users.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=255)
    text = RichTextUploadingField()
    slug = models.SlugField(unique=True)
    views = models.IntegerField(default=0)  
    likes = models.IntegerField(default=0) 
    date_time = models.DateTimeField(auto_now=True) 
    author = models.ForeignKey(User)
    category = models.ForeignKey('blog.Category', blank=True, null=True)
    tags = models.ManyToManyField('blog.Tag', blank=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        get_latest_by = "-date_time"
        ordering = ['-date_time', 'title']  

    def __str__(self):
        return self.title    

class Comment(models.Model):
    text = models.TextField(max_length=255)
    slug = models.SlugField(unique=True, null=True)
    author = models.ForeignKey(User, editable=False)
    date_time = models.DateTimeField(auto_now=True) 
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, blank=True, null=True)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        get_latest_by = "date_time"
        ordering = ['-post', 'date_time']

    def __str__(self):
        return "User %s at %s" % (self.author, self.post)     


class Category(models.Model):
   title = models.CharField(max_length=255)
   description = RichTextField()
   slug = models.SlugField(unique=True, null=True)

   class Meta:
       verbose_name = "Category"
       verbose_name_plural = "Categories"

   def __str__(self):
       return self.title
       
class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, null=True)  

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.title
                                                        