# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comments, Friendship, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'mentioned_user', 'content', 'date_posted', 'author')

class CommentsSerializer(serializers.ModelSerializer):
    user_commented = UserSerializer(read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'post_id', 'comment', 'user_commented', 'upvote', 'downvote')

class FriendshipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    friend = UserSerializer(read_only=True)

    class Meta:
        model = Friendship
        fields = ('friendship_id', 'user', 'friend', 'status', 'created_at')

class FriendRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)

    class Meta:
        model = FriendRequest
        fields = ('request_id', 'sender', 'receiver', 'status', 'created_at')
