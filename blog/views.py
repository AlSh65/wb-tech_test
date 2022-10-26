from djoser.serializers import UserSerializer
from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .paginator import PagePaginator
from .models import Post
from .serializers import PostSerializer




class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PagePaginator


