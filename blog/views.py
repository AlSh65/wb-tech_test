from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .serializers import PostSerializer, UserSerializer
from .paginator import PagePaginator
from .models import Post

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PagePaginator

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer