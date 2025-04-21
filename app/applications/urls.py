from django.urls import path, include
from rest_framework import routers

from .views import TrainingApplicationViewSet

router = routers.DefaultRouter()
router.register(r'training-applications', TrainingApplicationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
