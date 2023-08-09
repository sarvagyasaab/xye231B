from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_endpoints, name="endpoint-list"),
    path('posts/', views.postList, name="post-list"),
    path('post/<int:pk>', views.postDetail, name="post-detail"),
    path('user/<int:pk>/', views.userDetail, name='user-detail'),
    path('users/', views.userList, name='user-list'),
    path('post/<int:pk>/mentioned_user/', views.mentioned_user, name='mentioned_user'),
    path('post/<int:fk>/comments/', views.comment_views, name='comment-detail'),
]