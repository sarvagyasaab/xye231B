from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_posts, name='blog-posts'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('posts/', views.PostList.as_view(), name='user-list'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='user-detail'),
]