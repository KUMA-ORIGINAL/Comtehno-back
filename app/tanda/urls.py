from django.urls import path
from .views import QuestionListAPIView

urlpatterns = [
    path("tanda/", QuestionListAPIView.as_view(), name="tanda-list"),
]
