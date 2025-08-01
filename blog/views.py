from django.shortcuts import render, redirect

from .forms import PostForm
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
#/blog/create/
def create(request):
    if request.method == "POST":
        # form의 칸에 정보를 다 넣고, 제출 버튼을 누른경우.
        #작성하다가 제출 버튼을 누른경우
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post1 = postform.save(commit=False)
            post1.title = post1.title + "홍길동 만세"
            post1.save()
            return redirect('/blog/')
            #정상값인 경우
    else: # get , 새글작성하기 버튼을 눌러서 create()함수로 들어온 경우
        postform = PostForm()
    return render(request,
                  template_name='blog/postform.html',
                  context={'postform':postform})

#/blog/createfake/
#글을 써보자
def createfake(request):
    post = Post()
    post.title = " 새싹 용산구"
    post.content="나진상가 3층"
    post.save()
    return redirect('index')


