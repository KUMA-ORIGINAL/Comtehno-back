from django.urls import path, include
from rest_framework.routers import DefaultRouter

from partners.views import PartnerViewSet, PartnerDocumentViewSet

router = DefaultRouter()
router.register('partners', PartnerViewSet, basename='partners')
router.register('partner-document', PartnerDocumentViewSet, basename='partner_documents')

urlpatterns = [
    path('', include(router.urls)),
]
