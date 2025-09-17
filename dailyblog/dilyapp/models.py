from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # auto-generate slug from name
        super().save(*args, **kwargs)
    def __str__(self):
       return self.name
        
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    content = models.TextField()
    image = models.ImageField(upload_to='articles/', blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    is_published = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.title



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        author_name = self.author.username if self.author else "Anonymous"
        return f"Comment by {author_name} on {self.article}"