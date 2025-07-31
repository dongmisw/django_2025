#blog/forms.py
from django import forms
from blog.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'uploaded_image' ]

class PostForm1(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'uploaded_image' ]