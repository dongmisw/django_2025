from django.shortcuts import render
from .models import Post
# Create your views here.

#함수 생성
def index(request):
    #db에서 query - select * from post
    posts1111 = Post.objects.all().order_by('-pk')
    return render(request,
                  'blog/index.html',
                  context={'posts':posts1111}
                 )
def detail(request, pk):
    post1111 = Post.objects.get(pk=pk)
    return render(request,
                  'blog/detail.html',
                  context={'post2':post1111})