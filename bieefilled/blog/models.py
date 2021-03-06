from turtle import title
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title= models.CharField(max_length=200, unique=True)
    text=models.TextField((""))
    author= models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    created_date=models.DateTimeField(auto_now_add=True)
    
    class Created:
        ordering= ['-crated_on']
    def __str__(self):
        return self.title

