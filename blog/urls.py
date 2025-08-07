from django.urls import path
from . import views
#from .views import PostListView, PostCreateView, PostDetailView

urlpatterns=[

    path('',views.PostListView.as_view(),name='post-list'),
    path('<int:pk>/',views.PostDetailView.as_view(),name='post-detail'),
    path('create/', views.PostCreateView.as_view(),name='post-create'),
    path('<int:pk>/update/', views.PostUpdateView.as_view(),
         name='post-update'),
    path('<int:pk>/delete/', views.PostDeleteView.as_view(),
         name='post-delete'),

    #path('', views.index , name='index'),
    #path('<int:pk>/', views.detail ),
    #path('create/', views.create , name='blogcreate'),
    #path('<int:pk>/delete/',views.delete, name='blogdelete'),
    #path('<int:pk>/update/',views.update , name='blogupdate'),

    path('category/<slug>/', views.category, name='category'),

    path('tag/<slug>/',views.tag,name='tag'),

    path('<int:pk>/deletecomment', views.deletecomment, name='deletecomment'),
    path('<int:pk>/updatecomment', views.updatecomment, name='updatecomment'),
    path('<int:pk>/createcomment/',views.createcomment,name='createcomment'),

    path('createfake/', views.createfake),
]