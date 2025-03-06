from django.urls import path
from .views import FAQItemViewSet

urlpatterns = [
    path('FAQ/', FAQItemViewSet.as_view({'get': 'list'}), name='FAQ-list'),
]
