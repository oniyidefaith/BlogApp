from cgitb import text
from datetime import datetime
from operator import length_hint
from time import timezone
from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length =200)
    description = models.TextField()


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    Created_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    Published_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title

