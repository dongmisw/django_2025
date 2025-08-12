from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        UserPassesTestMixin)
from django.shortcuts import render, redirect
from django.views.generic import (ListView,
                                  CreateView,
                                  DetailView,
                                  UpdateView,
                                  DeleteView)
from .forms import PostForm, CommentForm
from .models import Post, Category, Tag, Comment

class PostDeleteView(LoginRequiredMixin,
                     UserPassesTestMixin,
                     DeleteView):
    model = Post
    success_url = '/blog/'
    #template_name = 'post_confirm_delete.html'
    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title','content','category',
              'uploaded_image','uploaded_file']
    #template_name = 'blog/post_form.html'

class PostDetailView(DetailView):
    model = Post
    # template_name = '/blog/post_detail.html'
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        context['commentform'] = CommentForm()
        return context

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content','category',
              'uploaded_image','uploaded_file']

    # template_name = 'blog/post_form.html'
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated:
            form.instance.author = current_user
            return super(PostCreateView, self).form_valid(form)
        else:
            return redirect('/blog/')

        #super.form_valid()
    #post_form.html

class PostListView(ListView):
    model = Post
    ordering = '-pk'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    #template_name = '/blog/post_list.html'
    # context -> post들  -> post_list
    #모델명에 따라서 대문자->소문자_list
    # Comment --> comment_list



# Create your views here.

#함수 생성
def index(request):
    #db에서 query - select * from post
    posts = Post.objects.all().order_by('-pk')
    categories = Category.objects.all()
    return render(request,
                  'blog/index.html',
                  context={'posts' : posts,
                           'categories' :categories
                           }
                 )
#/blog/category/<str:slug>/
#/blog/category/no_category
def category(request, slug):
    categories = Category.objects.all()
    if slug=='no_category':
        #미분류인경우
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


@login_required(login_url='/accounts/google/login/')
def detail(request, pk):
    post = Post.objects.get(pk=pk)
    categories = Category.objects.all()
    comments = Comment.objects.filter(post=post)
    commentform = CommentForm()
    return render(request,
                  'blog/detail.html',
                  context={'post':post,
                           'categories':categories,
                           'comments':comments,
                           'commentform':commentform
                           })
#/blog/create/
@login_required(login_url='/accounts/google/login/')
def create(request):

    categories = Category.objects.all()
    if request.method == "POST":
        # form의 칸에 정보를 다 넣고, 제출 버튼을 누른경우.
        #작성하다가 제출 버튼을 누른경우
        postform = PostForm(request.POST, request.FILES)
        if postform.is_valid():
            post1 = postform.save(commit=False)
            #post1.title = post1.title+'홍길동'
            post1.author = request.user
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

#/blog/<int:pk>/delete
@login_required(login_url='/accounts/google/login/')
def delete(request,pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('index')
#/blog/<int:pk>/update  -> pk는 post.pk
@login_required(login_url='/accounts/google/login/')
def update(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        postform = PostForm(request.POST, request.FILES, instance=post)
        if postform.is_valid():
            postform.save()
            return redirect('/blog/')
    else:
        postform = PostForm(instance=post)
    return render(request,
                  template_name='blog/postupdateform.html',
                  context={'postform':postform,}
                  )
def tag(request,slug):
    tag = Tag.objects.get(slug=slug)
    posts = Post.objects.filter(tags=tag)
    categories = Category.objects.all()
    return render(request,
                  'blog/index.html',
                  context={'posts':posts,
                           'categories':categories})

@login_required(login_url='/accounts/google/login/')
def createcomment(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment = commentform.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(post.get_absolute_url())
    return redirect(post.get_absolute_url())

@login_required(login_url='/accounts/google/login/')
def updatecomment(request,pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    if request.method == "POST":
        commentform = CommentForm(request.POST)
        if commentform.is_valid():
            comment1 = commentform.save(commit=False)
            comment1.post = post
            comment1.save()
            return redirect(post.get_absolute_url())
    else:
        commentform = CommentForm(instance=comment)
    return render(request,
                  template_name='blog/commentform.html',
                  context={'commentform':commentform,})

@login_required(login_url='/accounts/google/login/')
def deletecomment(request,pk):
    comment = Comment.objects.get(pk=pk)
    post = comment.post
    comment.delete()
    return redirect(post.get_absolute_url())