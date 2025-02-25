from django.urls import path
from .views import StudentReviewListView, StudentReviewDetailView, CategoryListView

urlpatterns = [
    path('reviews/', StudentReviewListView.as_view(), name='reviews-list'),
    path('reviews/<slug:slug>/', StudentReviewDetailView.as_view(), name='review-detail'),
    path('reviews-category/', CategoryListView.as_view(), name='category-list'),
]
