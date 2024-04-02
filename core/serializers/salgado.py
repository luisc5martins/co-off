from rest_framework.serializers import ModelSerializer

from core.models import Salgado


class SalgadoSerializer(ModelSerializer):
    class Meta:
        model = Salgado
        fields = "__all__"