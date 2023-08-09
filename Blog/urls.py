from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_endpoints, name="endpoint-list"),
    path('posts/', views.postList, name="post-list"),
    path('post/<int:pk>', views.postDetail, name="post-detail"),
    path('user/<int:pk>/', views.userDetail, name='user-detail'),
    path('post/comments/<int:pk>/', views.commentDetail, name='comment-detail'),
]