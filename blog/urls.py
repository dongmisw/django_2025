from django.urls import path
from . import views
urlpatterns=[
    #    127.0.0.1:8000/blog/
    path('', views.index , name='index'),
    path('<int:pk>/', views.detail ),
    path('create/', views.create , name='blogcreate'),
    #path('create/', views.create , name='blogcreate'),
    path('createfake/', views.createfake),
]