from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import StaffViewSet, StaffDepartmentViewSet

router = DefaultRouter()
router.register(r'staffs', StaffViewSet, basename='staff')
router.register(r'staff-departments', StaffDepartmentViewSet, basename='staff-departments')

urlpatterns = [
    path('', include(router.urls)),
]
