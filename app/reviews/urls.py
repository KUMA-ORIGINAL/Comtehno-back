from django.urls import path
from .views import StudentListAPIView, ReviewListAPIView

urlpatterns = [
    path('students/', StudentListAPIView.as_view(), name='api_students'),
    path('reviews/', ReviewListAPIView.as_view(), name='api_reviews'),
]
