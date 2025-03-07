from django.urls import path, include
from rest_framework import routers

from .views import ApplicantPageViewSet

router = routers.DefaultRouter()
router.register(r'applicant-pages', ApplicantPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]