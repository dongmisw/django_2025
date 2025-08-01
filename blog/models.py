from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,
                            unique=True,
                            allow_unicode=True)
    def __str__(self):
        return f'{self.name}----{self.slug}'



#blog/models.py
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL,
                               null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True)
    created_date = models.DateTimeField(auto_now_add=True,
                                        null=True)
    updated_date = models.DateTimeField(auto_now=True,
                                        null=True)
    uploaded_image = models.ImageField(upload_to='images/',
                                       blank=True)
    uploaded_file = models.FileField(upload_to='files/',
                                     blank=True)
    def __str__(self):
        return f'게시글제목: {self.title} -by {self.author} -category : {self.category} -  게시글내용 - {self.content} - 생성시간 - {self.created_date} - 업데이트-{self.updated_date}'
    def get_absolute_url(self):
        return f'/blog/{self.pk}/'