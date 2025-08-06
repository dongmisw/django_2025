from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from blog.models import Post
from example.serializers import PostSerializer


#http://localhost:8000/example/postAPI/3
@api_view(['GET','DELETE', 'PUT'])
def postAPI(request,pk):
    if request.method == 'GET':
        post = Post.objects.get(pk=pk)
        postSerializer = PostSerializer(post) #Post object -> json 바꿔야함. serializers.py
        return Response(postSerializer.data,
                        status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        post = Post.objects.get(pk=pk)
        post.delete()
        return Response("delete completed", status=status.HTTP_204_NO_CONTENT)
    else: # request.method == 'PUT'  수정하는 경우
        #post = Post.objects.get(pk=pk)
        post = get_object_or_404(Post, pk=pk)
        postSerializer = PostSerializer(post, data=request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data,
                            status=status.HTTP_200_OK)
    return Response(postSerializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET', 'POST'])
def blogAPI(request):
    if request.method == 'GET': #글 전체 리스트 보여주기
        posts = Post.objects.all()
        postSerializer = PostSerializer(posts, many=True)
        return Response(postSerializer.data,
                        status=status.HTTP_200_OK)
    else: #request.method == 'POST' ,  새글 쓰기.
        postSerializer = PostSerializer(data = request.data)
        if postSerializer.is_valid():
            postSerializer.save()
            return Response(postSerializer.data,
                            status = status.HTTP_201_CREATED)
    return Response(postSerializer.errors,
                    status = status.HTTP_400_BAD_REQUEST)
       #새로운 글 create 해준다.
    #화면에서 작성 json -> django 서버로 전달됨
    #json -> post instance 로 변경  - deserialize


@api_view(['GET'])
def helloAPI(request):
    return Response("hello world")

#example/views.py
# Create your views here.
def example(request):
    return render(request,
                  template_name ='example/example.html',
                  )
