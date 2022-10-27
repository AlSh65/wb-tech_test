from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, UserViewSet

router = DefaultRouter()
router.register('post', PostViewSet, basename='post')
router.register('user', UserViewSet, basename='user')
urlpatterns = [
    path('', include(router.urls)),
]
