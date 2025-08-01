from django.contrib import admin
from .models import Post, Category

#blog/admin.py
admin.site.register(Post)
admin.site.register(Category)


