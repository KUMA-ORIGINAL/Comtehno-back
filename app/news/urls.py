from django.urls import path, include
from rest_framework.routers import DefaultRouter

from news.views import PostViewSet, PostCategoryViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('posts-category', PostCategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
