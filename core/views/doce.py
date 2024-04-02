from rest_framework.viewsets import ModelViewSet

from core.models import Doce
from core.serializers import DoceSerializer


class DoceViewSet(ModelViewSet):
    queryset = Doce.objects.all()
    serializer_class = DoceSerializer