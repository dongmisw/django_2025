from django.contrib import admin
from .models import Post, Category, Comment, Tag
from markdownx.admin import MarkdownxModelAdmin
#blog/admin.py

admin.site.register(Tag)
admin.site.register(Post, MarkdownxModelAdmin)
admin.site.register(Category)
admin.site.register(Comment)

