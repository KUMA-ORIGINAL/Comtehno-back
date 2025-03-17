from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ParliamentMemberViewSet

router = DefaultRouter()
router.register(r'parliament-members', ParliamentMemberViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Теперь все API-доступы идут через `/api/members/`
]