from django.contrib.auth.models import User
from .models import Post, Comments
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model= Post
        fields = [
            'content',
            'date_posted',
            'author',
            'mentioned_user'
        ]
    @staticmethod
    def get_mentioned_user_name(self, obj):
        return obj.mentioned_user.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'date_joined',
            'is_active'
        ]

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'