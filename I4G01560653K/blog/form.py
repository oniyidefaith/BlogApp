from dataclasses import fields
from django import forms
from .models import Blog
from .models import Post

class BlogForm(forms.ModelForm):
    

    class Meta:
        model = Blog
        fields =[
            "title",
            "description",
        ]
    
    class Metas:
        model = Post
        fields = [
           "author",
            "text",
            "Created_date",
            "Published_date",
        ]