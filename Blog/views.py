import hashlib
import random

import rest_framework
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework import viewsets, status, mixins, generics, filters
from rest_framework.decorators import action, api_view
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
        email = request.data.get('email', '')

        if not email.endswith('@rvce.edu.in'):
            return Response({'detail': 'Email must end with @rvce.edu.in'}, status=status.HTTP_400_BAD_REQUEST)

        hashed_password = make_password(request.data['password'])
        request.data['password'] = hashed_password
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'detail': f'User registered successfully: {user}'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        email = request.data.get('email', '')

        if not email.endswith('@rvce.edu.in'):
            return Response({'detail': 'Email must end with @rvce.edu.in'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            # Try to retrieve by user ID
            user = get_object_or_404(User, pk=pk)
        except Http404:
            # If not found by user ID, try to retrieve by username
            user = get_object_or_404(User, username=pk)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def find_user(self, request):
        # Implement your custom logic to find users here
        # You can retrieve users based on certain criteria
        # For example, filtering users by username
        username = request.query_params.get('username', None)
        if username:
            users = User.objects.filter(username=username)
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['GET'])
    def user_details(self, request, pk=None):
        user = get_object_or_404(User, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date_posted')[:100]
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            mentioned_user_info = request.data.get('mentioned_user')
            mentioned_user = None

            if isinstance(mentioned_user_info, int):
                try:
                    mentioned_user = User.objects.get(pk=mentioned_user_info)
                except User.DoesNotExist:
                    mentioned_user = None
            elif isinstance(mentioned_user_info, str):
                try:
                    mentioned_user = User.objects.get(username=mentioned_user_info)
                except User.DoesNotExist:
                    mentioned_user = None

            serializer.validated_data['author'] = request.user
            serializer.validated_data['mentioned_user'] = mentioned_user
            post = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieveByID(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def update(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = Friendship.objects.all()
    serializer_class = FriendshipSerializer

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

    def create(self, request, *args, **kwargs):
        serializer = CommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            comment = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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

class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']
