from django.contrib.auth.views import PasswordResetView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import (
    UserViewSet,
    PostViewSet,
    FriendshipViewSet,
    FriendRequestViewSet,
    PostByUserViewSet,
    CommentsViewSet,
    UserSearchView,
)
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'friendships', FriendshipViewSet)
router.register(r'comments', CommentsViewSet)
router.register(r'friend-requests', FriendRequestViewSet, basename='friendrequest')

urlpatterns = [
    path('', include(router.urls)),
]

urlpatterns += [
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('api/users/search/', UserSearchView.as_view(), name='user-search'), #http://localhost:8000/api/users/search/?search=<name>/<email>
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('friend-requests/received/<str:user_identifier>/', FriendRequestViewSet.as_view({'get': 'received'}), name='received-friend-requests'),
    path('friend-requests/sent/<str:user_identifier>/', FriendRequestViewSet.as_view({'get': 'sent'}), name='sent-friend-requests'),
    path('posts-by-user/<str:username>/', PostByUserViewSet.as_view({'get': 'list'}), name='posts-by-user-list'),
    path('', include(router.urls)),
    path('users/<int:pk>/user-details/', UserViewSet.as_view({'get': 'user_details'}), name='user-details'),
]

'''
    Create User: POST /users/
    Retrieve User: GET /users/{user_id}/
    Update User: PUT /users/{user_id}/
    Delete User: DELETE /users/{user_id}/
    Find User: GET /users/find_user/?username={username}
'''

'''
    List all posts: GET /posts/
    Create a new post: POST /posts/
    Retrieve a specific post: GET /posts/{post_id}/
    Update a specific post: PUT /posts/{post_id}/
    Partially update a specific post: PATCH /posts/{post_id}/
    Delete a specific post: DELETE /posts/{post_id}/
'''