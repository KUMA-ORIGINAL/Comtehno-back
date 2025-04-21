from rest_framework import viewsets, mixins
from .models import TrainingApplication
from .serializers import TrainingApplicationSerializer
from .utils import send_telegram_message


class TrainingApplicationViewSet(viewsets.GenericViewSet,
                                 mixins.CreateModelMixin,):
    queryset = TrainingApplication.objects.all()
    serializer_class = TrainingApplicationSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        send_telegram_message(
            f"📝 Новая заявка на обучение:\n\n"
            f"<b>Имя:</b> {instance.full_name}\n"
            f"<b>Email:</b> {instance.email}\n"
            f"<b>Номер телефона:</b> {instance.phone}\n"
            f"<b>Комментарий</b> {instance.comment}\n"
        )