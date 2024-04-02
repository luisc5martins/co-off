from rest_framework.viewsets import ModelViewSet

from core.models import Salgado
from core.serializers import SalgadoSerializer


class SalgadoViewSet(ModelViewSet):
    queryset = Salgado.objects.all()
    serializer_class = SalgadoSerializer