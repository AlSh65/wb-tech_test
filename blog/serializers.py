from djoser.serializers import UserSerializer
from rest_framework import serializers
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(UserSerializer):
    blog = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'blog']