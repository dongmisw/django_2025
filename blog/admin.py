from django.contrib import admin
from .models import Post, Category, Comment

#blog/admin.py
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment)

