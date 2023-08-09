from cryptography.fernet import Fernet
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
# from .models import Post, PostActivity, Comment
from .models import Post, Comments
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer, PostSerializer, CommentsSerializer
from http import HTTPStatus

def Home(request):
    message = 'Home Page'
    return HttpResponse("Home")

ENCRYPTION_KEY = b"PczoyJQgy_xRAnp_YNkecV6KGROpqDv94_6COdyHrT8='"

def encrypt_data(data):
    fernet = Fernet(ENCRYPTION_KEY)
    encrypted_data = fernet.encrypt(data.encode())
    return encrypted_data

def decrypt_data(encrypted_data):
    fernet = Fernet(ENCRYPTION_KEY)
    decrypted_data = fernet.decrypt(encrypted_data).decode()
    return decrypted_data

def all_posts(request):
    posts = Post.objects.select_related('author', 'mentioned_user').all()
    serialized_posts = []

    for post in posts:
        serialized_post = {
            "content": post.content,
            "date_posted": post.date_posted.strftime('%Y-%m-%d %H:%M:%S'),
            "author": encrypt_data(post.author.username).decode('utf-8'),
            "mentioned_user": None,
            "comments": [],
        }

        if post.mentioned_user:
            serialized_post["mentioned_user"] = {
                "username": post.mentioned_user.username,
            }

        comments = Comments.objects.filter(post_id=post.id).select_related('user_commented')

        post_comments = []
        for comment in comments:
            comment_data = {
                'comment-user': comment.user_commented.username,
                'comment-data': comment.comment,
                'upvote' : comment.upvote,
                'downvote' : comment.downvote
            }
            post_comments.append(comment_data)

        serialized_post['comments'] = post_comments
        serialized_posts.append(serialized_post)

    return JsonResponse(serialized_posts, safe=False)

# add constraints to model Comments (done)
# add upvote/downvote to json (done)


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from .models import User, Post
from .serializers import UserSerializer, PostSerializer

@api_view(['GET'])
def all_endpoints(request):
    endpoints = {
        'all_endpoints': '/',
    }
    return Response(endpoints)

@api_view(['GET'])
def userDetail(request, pk):
    try:
        user_info = User.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user_info)
    return Response(serializer.data)

@api_view(['GET'])
def postList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def postDetail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except ObjectDoesNotExist:
        return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(post, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def comment_views(request, fk):
    try:
        comments = Comments.objects.filter(post_id=fk)
    except ObjectDoesNotExist:
        return Response({"message": "NO COMMENTS"}, status=status.HTTP_204_NO_CONTENT)

    all_comments = []
    for i, comment in enumerate(comments):
        serializer = CommentsSerializer(comment, many=False)  # Use CommentSerializer for each comment
        all_comments.append(serializer.data)

    return Response(all_comments)


