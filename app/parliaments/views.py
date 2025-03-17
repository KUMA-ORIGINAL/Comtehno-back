from rest_framework import viewsets, mixins

from .models import ParliamentMember
from .serializers import ParliamentMemberSerializer


class ParliamentMemberViewSet(viewsets.GenericViewSet,
                              mixins.ListModelMixin):
    queryset = ParliamentMember.objects.filter(is_hidden=False)
    serializer_class = ParliamentMemberSerializer
