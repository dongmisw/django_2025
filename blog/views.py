from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView,CreateView,UpdateView,DeleteView

from .forms import PostForm
from .models import Post, Category

# Create your views here.

#함수 생성
def index(request):
    #db에서 query - select * from post
    posts1111 = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request,
                  'blog/index.html',
                  context={'posts' : posts1111,
                           'categories' :categories
                           }
                 )
#/blog/category/<str:slug>/
#/blog/category/no_category
def category(request, slug):
    categories = Category.objects.all()
    if slug=='no_category':
        #미분류인경우ㅠ
        posts= Post.objects.filter(category=None)
    else: # 맛집, 용산구
        category = Category.objects.get(slug=slug)
        posts= Post.objects.filter(category=category)
    return render(request,
                  template_name='blog/index.html',
                  context={'posts': posts,
                           'categories': categories
                           }
                  )

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    return render(request,
                  'blog/detail.html',
                  context={'post':post,
                           'categories':categories
                           })
#/blog/create/
def create(request):

    categories = Category.objects.all()
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
                  context={'postform':postform,
                           'categories':categories}
                  )

#/blog/createfake/
#글을 써보자
def createfake(request):
    post = Post()
    post.title = " 새싹 용산구"
    post.content="나진상가 3층"
    post.save()
    return redirect('index')


