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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name'
        ]