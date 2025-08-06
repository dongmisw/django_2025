# example/urls.py
from django.urls import path
from . import views
urlpatterns =[
    path('',views.example, name='example'),
    path('helloAPI/', views.helloAPI, name='helloAPI'),
    #example/postAPI/{post:pk}/ 	=> 'GET'  ->  3번글 상세보기
    path('postAPI/<int:pk>/', views.postAPI, name='postAPI'),
    path('blogAPI/', views.blogAPI, name='blogAPI'),
]