from django.urls import path
from . import views
urlpatterns=[
    path('category/<slug>/',views.category,name='category'),
    path('', views.index , name='index'),
    path('<int:pk>/', views.detail ),
    #path('create/', views.create , name='blogcreate'),
    path('create/', views.create , name='blogcreate'),
    #path('create/', views.create , name='blogcreate'),
    path('createfake/', views.createfake),
]