from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import EventViewSet, EventCategoryViewSet, TeamCreateViewSet

router = DefaultRouter()
router.register('events-team', TeamCreateViewSet, basename='teams')
router.register('events', EventViewSet, basename='events')
router.register('events-category', EventCategoryViewSet, basename='events_category')


urlpatterns = [
    path('', include(router.urls)),
]
