import hashlib

import rest_framework
from django.contrib.auth.hashers import make_password
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.models import User

from . import serializers
from .models import Post, Comments, Friendship, FriendRequest
from .serializers import (
    PostSerializer,
    CommentsSerializer,
    FriendshipSerializer,
    FriendRequestSerializer,
    UserSerializer,
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        hashed_password = make_password(request.data['password'])
        request.data['password'] = hashed_password
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')[:100]
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            post = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

class FriendRequestViewSet(viewsets.ModelViewSet):
    serializer_class = FriendRequestSerializer
    def get_queryset(self):
        user_identifier = self.kwargs.get('user_identifier')
        try:
            user_id = int(user_identifier)
            user_obj = get_object_or_404(User, id=user_id)
        except ValueError:
            user_obj = get_object_or_404(User, username=user_identifier)

        if self.action == 'received':
            return FriendRequest.objects.filter(receiver=user_obj)
        elif self.action == 'sent':
            return FriendRequest.objects.filter(sender=user_obj)
        return FriendRequest.objects.none()

    @action(detail=False, methods=['GET'], name='Received Friend Requests')
    def received(self, request, user_identifier=None):
        return self.list(request, user_identifier=user_identifier)

    @action(detail=False, methods=['GET'], name='Sent Friend Requests')
    def sent(self, request, user_identifier=None):
        return self.list(request, user_identifier=user_identifier)

class PostByUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        username = self.kwargs.get('username')
        user = get_object_or_404(User, username=username)
        return Post.objects.filter(author=user)

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    author = rest_framework.serializers.ReadOnlyField(source='author.username')  # Make the author field read-only

    class Meta:
        model = Comments
        fields = '__all__'

    def list(self, request, post_id=None):
        comments = Comments.objects.filter(post_id=post_id)
        serializer = CommentsSerializer(comments, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            comment = serializer.save(author=request.user)  # Set the author to the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


