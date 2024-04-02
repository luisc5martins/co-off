from rest_framework.viewsets import ModelViewSet

from core.models import Cafe
from core.serializers import CafeSerializer


class CafeViewSet(ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer