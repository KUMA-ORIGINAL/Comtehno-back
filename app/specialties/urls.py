from django.urls import path, include
from rest_framework.routers import DefaultRouter

from specialties import views

router = DefaultRouter()
router.register(r'specialties', views.SpecialtyViewSet)
router.register(r'specialties-category', views.SpecialtyCategoryViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
