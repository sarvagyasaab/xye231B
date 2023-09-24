# serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comments, Friendship, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password')

class UserField(serializers.RelatedField):
    def to_internal_value(self, data):
        try:
            return User.objects.get(pk=int(data))
        except (ValueError, User.DoesNotExist):
            try:
                return User.objects.get(username=data)
            except User.DoesNotExist:
                raise serializers.ValidationError("User not found")

    def to_representation(self, obj):
        return obj.username

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    mentioned_user = UserField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Post
        fields = ('id', 'mentioned_user', 'content', 'date_posted', 'author', 'color_code')

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'

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
