from rest_framework import viewsets, mixins
from .models import TrainingApplication
from .serializers import TrainingApplicationSerializer


class TrainingApplicationViewSet(viewsets.GenericViewSet,
                                 mixins.CreateModelMixin,):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer

