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
    path('<int:pk>/delete/',
         views.delete, name='blogdelete'),
    path('<int:pk>/update/',
         views.update , name='blogupdate'),
    path('tag/<slug>/',views.tag,name='tag'),

    path('<int:pk>/deletecomment', views.deletecomment, name='deletecomment'),
    path('<int:pk>/updatecomment', views.updatecomment, name='updatecomment'),
    path('<int:pk>/createcomment/',views.createcomment,name='createcomment'),
]